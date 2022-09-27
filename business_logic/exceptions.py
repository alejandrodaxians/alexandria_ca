class ConnectionError(Exception):
    def __init__(self, message: str, code: int) -> None:
        super().__init__()
        self.message = message
        self.code = code


class RequestError(Exception):
    def __init__(self, message: str, code: int) -> None:
        super().__init__()
        self.message = message
        self.code = code
