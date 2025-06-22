from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
BASE = "/api/v1/stringutils"


def test_ascii() -> None:
    resp = client.post(f"{BASE}/ascii", json={"text": "Olá, Café!"})
    assert resp.status_code == 200
    assert resp.json() == {"result": "Ola, Cafe!"}


def test_ascii_unicode() -> None:
    resp = client.post(f"{BASE}/ascii", json={"text": "漢字�"})
    assert resp.status_code == 200
