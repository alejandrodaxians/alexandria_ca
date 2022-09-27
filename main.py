from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse


from adapters.endpoints.books_ep import router
from adapters.exceptions.excp_handlers import server_excp_handler, book_not_found_excp_handler
from business_logic.config.properties import APP_DESCRIPTION, APP_TITLE, BACKEND_URL
from adapters.exceptions.exceptions import ServerError, BookNotFoundError
from adapters.connectors.db_connection import DatabaseConnection


db = DatabaseConnection()


app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[BACKEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

app.add_exception_handler(ServerError, server_excp_handler)
app.add_exception_handler(BookNotFoundError, book_not_found_excp_handler)


@app.get("/", include_in_schema=False)
def root():
    # return {"message": "App Running"}
    return RedirectResponse(url="/docs")
