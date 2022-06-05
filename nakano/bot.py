import asyncio

from aiohttp import ClientSession
from . import GatewayClient

__all__ = ["BotBase"]


class BotBase(GatewayClient):

    def __init__(self, intents: int, loop: asyncio.AbstractEventLoop, session: ClientSession) -> None:
        super().__init__(intents, loop, session)
