from dataclasses import dataclass

from .baseobject import BaseObject


__all__ = ["SnowFlake"]

@dataclass
class SnowFlake(BaseObject):

    id: int
