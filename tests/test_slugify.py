from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
BASE = "/api/v1/stringutils"


def test_slugify() -> None:
    resp = client.post(f"{BASE}/slugify", json={"text": "Olá Mundo!"})
    assert resp.status_code == 200
    assert resp.json() == {"result": "ola-mundo"}
