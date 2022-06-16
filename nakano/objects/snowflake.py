from dataclasses import dataclass
from typing import ClassVar

from .baseobject import BaseObject


__all__ = ["SnowFlake"]

@dataclass
class SnowFlake(BaseObject):

    id: ClassVar[int] = 0

    def __str__(self) -> str:
        return str(self.id)
    
    def __repr__(self) -> str:
        return super().__repr__()

