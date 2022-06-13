from typing import TYPE_CHECKING, Any

__all__ = ["EventManager"]

if TYPE_CHECKING:
    from .gatewayclient import GatewayClient


class EventManager:
    def __init__(self, gatewayclient: GatewayClient) -> None:
        self.gatewayclient = gatewayclient

    async def checker(self, eventpayload: dict[str, Any]) -> None:
        eventop = eventpayload["op"]
        if eventop == 11:
            pass
        elif eventop == 1:
            await self.gatewayclient.send_heartbeat()
        for d in self.gatewayclient.listeners:
            eventname = eventpayload["t"]
            if coro := d.get(eventname):
                await coro(eventpayload["d"])
