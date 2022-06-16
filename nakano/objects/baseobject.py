__all__ = ["BaseObject"]



from typing import TYPE_CHECKING, ClassVar
import datetime

if TYPE_CHECKING:
    from .snowflake import SnowFlake


class BaseObject:

    snowflake: ClassVar[None | SnowFlake] = None

    def __repr__(self) -> str:
        return f"<OBJECT_TYPE={self.__class__.__name__} ID={self.snowflake}>"
    
    def snowflake_time(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(timestamp = ((self.snowflake.id >> 22) +  1420070400000) / 1000, tz=datetime.timezone.utc)
