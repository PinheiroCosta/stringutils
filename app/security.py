import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def configure_security(app: FastAPI) -> None:
    origins_env = os.getenv("CORS_ORIGINS", "")
    origins = [
        origin.strip() for origin in origins_env.split(",") if origin.strip()
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
