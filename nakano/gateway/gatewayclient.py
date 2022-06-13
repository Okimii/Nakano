from __future__ import annotations

import asyncio
import json
import random
import sys
from typing import Any, Awaitable, Callable

from aiohttp import ClientSession

from nakano.httpclient import HTTPClient, Route
from nakano.errors import OutdatedGatewayVersion, InvalidGatewayEventName
from .eventmanagement import EventManager
from .gatewayenum import GatewayEvents
__all__ = ["GatewayClient"]
Coro = Callable[..., Awaitable[Any]]


class GatewayClient:
    def __init__(
        self,
        intents: int,
        loop: asyncio.AbstractEventLoop,
        session: ClientSession,
        gatewayver: int = 10,
    ) -> None:
        self.intents = intents
        self.http = HTTPClient(session)
        self.loop = loop or (asyncio.get_running_loop() or asyncio.new_event_loop())
        self.gatewayver = gatewayver
        self.sequence = None
        self.listeners: list[Coro] = []
        if gatewayver not in {9, 10}:
            raise OutdatedGatewayVersion(
                f"Gateway version must be between 9 or 10, not {gatewayver}."
            )

    def on(self, eventname: str) -> Coro:
        def register(coro: Coro) -> Coro:
            if not asyncio.iscoroutinefunction(coro):
                raise TypeError("event registered must be a coroutine function")
            if eventname not in GatewayEvents.all_events():
                raise InvalidGatewayEventName(f"Incorrect gateway event name, please check spelling and remember gateway event names are formatted in UPPERCASE and snake_casing.")
            self.listeners.append({eventname: coro})
            return coro

        return register

    async def connect(self) -> None:
        gateway_bot = await self.http.request_(
            Route("GET", "gateway/bot", {"Authorization": f"Bot {self.token}"})
        )
        self.shards = gateway_bot["shards"]
        self.ws = await self.http.session.ws_connect(
            f"{gateway_bot['url']}?v={self.gatewayver}&encoding=json"
        )
        await self.identify()
        self.hb_interval = (await self.ws.receive_json())["d"][
            "heartbeat_interval"
        ] / 1000

    async def close(self) -> None:
        await self.ws.close()
        await self.http.session.close()

    @property
    def jitter(self) -> float:
        return random.random()

    async def heart(self) -> None:
        while not self.ws.closed:
            await self.send_heartbeat()
            await asyncio.sleep(self.jitter * float(self.hb_interval))

    async def startup(self, token: str) -> None:
        self.token = token
        await self.connect()
        self.loop.create_task(self.heart())
        await self.eventhandler()

    async def send_heartbeat(self) -> None:
        await self.ws.send_json({"op": 1, "d": self.sequence})

    async def identify(self) -> None:
        await self.ws.send_json(
            {
                "op": 2,
                "d": {
                    "token": self.token,
                    "intents": self.intents,
                    "properties": {
                        "$os": sys.platform,
                        "$browser": "Nakano",
                        "$device": "Nakano",
                    },
                },
            }
        )

    async def eventhandler(self) -> None:
        eventmang = EventManager(self)
        async for event in self.ws:
            await eventmang.checker(json.loads(event[1]))
