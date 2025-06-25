import logging
import traceback
from fastapi import Request
from fastapi.responses import JSONResponse

logging.basicConfig(level=logging.ERROR)


async def generic_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unhandled error: {exc}\n{traceback.format_exc()}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"},
    )
