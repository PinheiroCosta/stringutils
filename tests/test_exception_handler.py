from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient
from app.exception_handlers import generic_exception_handler


def raise_runtime_error():
    raise RuntimeError("Forced error for testing")


def create_test_app() -> FastAPI:
    app = FastAPI()
    app.add_exception_handler(Exception, generic_exception_handler)

    @app.get("/force-error")
    def force_error(_: None = Depends(raise_runtime_error)):
        return {"ok": True}

    return app


def test_generic_exception_handler() -> None:
    app = create_test_app()
    client = TestClient(app, raise_server_exceptions=False)

    resp = client.get("/force-error")
    assert resp.status_code == 500
    assert resp.json() == {"error": "Internal server error"}
