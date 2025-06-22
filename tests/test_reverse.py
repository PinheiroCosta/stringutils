from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
BASE = "/api/v1/stringutils"


def test_reverse() -> None:
    resp = client.post(f"{BASE}/reverse", json={"text": "abc"})
    assert resp.status_code == 200
    assert resp.json() == {"result": "cba"}


def test_reverse_empty() -> None:
    resp = client.post(f"{BASE}/reverse", json={"text": ""})
    assert resp.status_code == 422


def test_reverse_missing_field() -> None:
    resp = client.post(f"{BASE}/reverse", json={})
    assert resp.status_code == 422
