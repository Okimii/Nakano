class BaseObject:

    def __repr__(self) -> str:
        return f"ID: {self.id}, OBJECT_TYPE: {self.__class__.__name__}"
