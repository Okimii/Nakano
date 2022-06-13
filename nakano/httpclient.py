from dataclasses import dataclass
from typing import Any, ClassVar

import aiohttp

__all__ = ["Route", "HTTPClient"]


@dataclass
class Route:
    BASEURL: ClassVar = "https://discord.com/api/v10"
    method: str
    endpoint: str
    headers: dict[Any, Any]


class HTTPClient:
    def __init__(self, session: aiohttp.ClientSession) -> None:
        self.session = session

    async def request_(self, route: Route) -> dict[str, Any]:
        async with self.session.request(
            route.method, f"{route.BASEURL}/{route.endpoint}", headers=route.headers
        ) as payload:
            return await payload.json()
