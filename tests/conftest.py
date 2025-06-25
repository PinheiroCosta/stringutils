import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.v1 import endpoints
from app.exception_handlers import generic_exception_handler
from app.security import configure_security
from app.utils import get_version


def create_test_app() -> FastAPI:
    app = FastAPI(title="StringUtils API (Test)", version=get_version())
    configure_security(app)
    app.include_router(
        endpoints.router,
        prefix="/api/v1/stringutils",
        tags=["stringutils"],
    )
    app.add_exception_handler(Exception, generic_exception_handler)
    return app


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("CORS_ORIGINS", "https://example.com")
    app = create_test_app()
    return TestClient(app)
