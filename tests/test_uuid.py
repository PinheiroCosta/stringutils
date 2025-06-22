from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)
BASE = "/api/v1/stringutils"


def test_uuid() -> None:
    resp = client.post(f"{BASE}/uuid")
    assert resp.status_code == 200
    result = resp.json()["result"]
    uuid_obj = uuid.UUID(result)
    assert str(uuid_obj) == result
