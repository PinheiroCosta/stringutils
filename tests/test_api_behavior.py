from fastapi.testclient import TestClient
from app.main import app
import time

client = TestClient(app)
BASE = "/api/v1/stringutils"


def test_response_content_type() -> None:
    resp = client.post(f"{BASE}/reverse", json={"text": "abc"})
    assert resp.headers["content-type"].startswith("application/json")


def test_response_time_under_500ms() -> None:
    start = time.time()
    resp = client.post(f"{BASE}/reverse", json={"text": "abc"})
    duration = time.time() - start
    assert resp.status_code == 200
    assert duration < 0.5


def test_unexpected_server_error_handling() -> None:
    # Tentando forçar um 500 por falta de campo obrigatório em /charcount
    resp = client.post(f"{BASE}/charcount", json={})
    # Espera-se 422, não 500
    assert resp.status_code == 422
