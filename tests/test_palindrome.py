from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
BASE = "/api/v1/stringutils"


def test_palindrome_true() -> None:
    resp = client.post(
        f"{BASE}/palindrome",
        json={"text": "A man, a plan, a canal: Panama"}
    )
    assert resp.status_code == 200
    assert resp.json() == {"result": True}


def test_palindrome_false() -> None:
    resp = client.post(f"{BASE}/palindrome", json={"text": "hello"})
    assert resp.status_code == 200
    assert resp.json() == {"result": False}
