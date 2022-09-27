from fastapi import Request
from fastapi.responses import JSONResponse

from adapters.exceptions.exceptions import ServerError, BookNotFoundError
from business_logic.config.logging.loggers import get_logger


api_logger = get_logger('main')


async def server_excp_handler(request: Request, nfe: ServerError):
    return JSONResponse(
        status_code=nfe.status_code,
        content=ServerError(
            message=nfe.message,
            status_code=nfe.status_code
        )
    )


async def book_not_found_excp_handler(request: Request, nfe: BookNotFoundError):
    return JSONResponse(
        status_code=nfe.status_code,
        content=BookNotFoundError(
            message=nfe.message,
            status_code=nfe.status_code
        )
    )
