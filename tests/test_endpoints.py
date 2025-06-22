from fastapi.testclient import TestClient
from app.main import app
from typing import Any, Dict, cast


client = TestClient(app)

BASE = "/api/v1/stringutils"


def test_reverse() -> None:
    resp = client.post(f"{BASE}/reverse", json={"text": "abc"})
    assert resp.status_code == 200
    assert resp.json() == {"result": "cba"}


def test_uppercase() -> None:
    resp = client.post(f"{BASE}/uppercase", json={"text": "abc"})
    assert resp.status_code == 200
    assert resp.json() == {"result": "ABC"}


def test_lowercase() -> None:
    resp = client.post(f"{BASE}/lowercase", json={"text": "ABC"})
    assert resp.status_code == 200
    assert resp.json() == {"result": "abc"}


def test_slugify() -> None:
    resp = client.post(f"{BASE}/slugify", json={"text": "Olá Mundo!"})
    assert resp.status_code == 200
    assert resp.json() == {"result": "ola-mundo"}


def test_uuid() -> None:
    resp = client.post(f"{BASE}/uuid")
    assert resp.status_code == 200
    assert "result" in resp.json()
    assert len(resp.json()["result"]) == 36


def test_ascii() -> None:
    resp = client.post(f"{BASE}/ascii", json={"text": "Olá, Café!"})
    assert resp.status_code == 200
    assert resp.json() == {"result": "Ola, Cafe!"}


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
    # characters count should differ if spaces and specials are excluded
    assert data["characters"] < len(cast(str, payload["text"]))
