from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
BASE = "/api/v1/stringutils"


def test_lowercase() -> None:
    resp = client.post(f"{BASE}/lowercase", json={"text": "ABC"})
    assert resp.status_code == 200
    assert resp.json() == {"result": "abc"}
