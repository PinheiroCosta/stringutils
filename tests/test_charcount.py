from fastapi.testclient import TestClient
from app.main import app
from typing import Any, Dict, cast

client = TestClient(app)
BASE = "/api/v1/stringutils"


def test_charcount_defaults() -> None:
    payload = {"text": "Hello, World! 123"}
    resp = client.post(f"{BASE}/charcount", json=payload)
    assert resp.status_code == 200
    data: Dict[str, Any] = resp.json()
    assert "characters" in data
    assert "words" in data
    assert "vowels" in data
    assert "consonants" in data


def test_charcount_options_false() -> None:
    payload = {
        "text": "Hello, World! 123",
        "count_spaces": False,
        "count_special": False,
        "count_escaped": False,
    }
    resp = client.post(f"{BASE}/charcount", json=payload)
    assert resp.status_code == 200
    data: Dict[str, int] = resp.json()
    assert data["characters"] < len(cast(str, payload["text"]))
