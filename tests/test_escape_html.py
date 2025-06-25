from fastapi.testclient import TestClient
from app.main import app
from typing import Dict

client = TestClient(app)
BASE = "/api/v1/stringutils"


def test_escape_html_basic() -> None:
    payload = {"text": "<div>5 < 10 & 'ok'</div>"}
    resp = client.post(f"{BASE}/escape-html", json=payload)
    assert resp.status_code == 200
    data: Dict[str, str] = resp.json()
    assert data["result"] == "&lt;div&gt;5 &lt; 10 &amp; 'ok'&lt;/div&gt;"


def test_escape_html_empty() -> None:
    payload = {"text": ""}
    resp = client.post(f"{BASE}/escape-html", json=payload)
    assert resp.status_code == 422


def test_escape_html_no_special_chars() -> None:
    payload = {"text": "Texto sem HTML e com 'aspas' normais"}
    resp = client.post(f"{BASE}/escape-html", json=payload)
    assert resp.status_code == 200
    data: Dict[str, str] = resp.json()
    assert data["result"] == "Texto sem HTML e com 'aspas' normais"


def test_escape_html_already_escaped() -> None:
    payload = {"text": "&lt;div&gt;"}
    resp = client.post(f"{BASE}/escape-html", json=payload)
    assert resp.status_code == 200
    data: Dict[str, str] = resp.json()
    assert data["result"] == "&amp;lt;div&amp;gt;"
