from fastapi import status

from business_logic.exceptions import RequestError


class LibraryError(RequestError):

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return repr(self.message)


class ServerError(LibraryError):
    def __init__(self, message: str, status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR):
        super().__init__(
            message=message,
            status_code=status_code,
        )


class BookError(LibraryError):
    def __init__(self, message: str):
        super().__init__(message)


class BookNotFoundError(BookError):
    def __init__(self, message: str, status_code: int = status.HTTP_404_NOT_FOUND):
        super().__init__(
            message=message,
            status_code=status_code,
        )
