class BaseNakanoException(Exception):
    
    def __init__(self, message: str = "") -> None:
        super().__init__(message)

class OutdatedGatewayVersion(BaseNakanoException):

    def __init__(self, message: str = "") -> None:
        super().__init__(message)