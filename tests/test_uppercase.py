from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
BASE = "/api/v1/stringutils"


def test_uppercase() -> None:
    resp = client.post(f"{BASE}/uppercase", json={"text": "abc"})
    assert resp.status_code == 200
    assert resp.json() == {"result": "ABC"}
