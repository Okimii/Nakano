import asyncio

from aiohttp import ClientSession
from gateway.gatewayclient import GatewayClient


class BotBase(GatewayClient):

    def __init__(self, intents: int, loop: asyncio.AbstractEventLoop, session: ClientSession) -> None:
        super().__init__(intents, loop, session)
