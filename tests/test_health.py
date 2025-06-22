from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
BASE = "/api/v1/stringutils"


def test_health_check() -> None:
    resp = client.get(f"{BASE}/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}
