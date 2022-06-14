__all__ = ["BaseObject"]

class BaseObject:

    def __repr__(self) -> str:
        return f"<OBJECT_TYPE={self.__class__.__name__} ID={self.id}>"
