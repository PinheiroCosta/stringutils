from fastapi.testclient import TestClient
from app.main import app
from tests.conftest import create_test_app


def test_cors_allows_configured_origin(client):
    response = client.options(
        "/api/v1/stringutils/health",
        headers={
            "Origin": "https://example.com",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert response.status_code == 200
    assert response.headers.get("access-control-allow-origin") == "https://example.com"


def test_cors_blocks_unallowed_origin(client):
    response = client.options(
        "/api/v1/stringutils/health",
        headers={
            "Origin": "https://malicious-site.com",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert "access-control-allow-origin" not in response.headers
