# app/security.py
import os
from fastapi.middleware.cors import CORSMiddleware

def configure_security(app):
    origins_env = os.getenv("CORS_ORIGINS", "")
    origins = [origin.strip() for origin in origins_env.split(",") if origin.strip()]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
