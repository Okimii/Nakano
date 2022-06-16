__all__ = ["BaseObject"]



from typing import ClassVar
import datetime


class BaseObject:

    id: ClassVar[int] = 0

    def __repr__(self) -> str:
        return f"<OBJECT_TYPE={self.__class__.__name__} ID={self.id}>"
    
    def snowflake_time(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(timestamp = ((self.id >> 22) +  1420070400000) / 1000, tz=datetime.timezone.utc)