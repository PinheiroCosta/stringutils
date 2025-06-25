from fastapi import FastAPI
from app.utils import get_version
from app.api.v1 import endpoints
from app.exception_handlers import generic_exception_handler
from app.security import configure_security


app = FastAPI(title="StringUtils API", version=get_version())

configure_security(app)

app.include_router(
    endpoints.router,
    prefix="/api/v1/stringutils",
    tags=["stringutils"]
)

app.add_exception_handler(Exception, generic_exception_handler)
