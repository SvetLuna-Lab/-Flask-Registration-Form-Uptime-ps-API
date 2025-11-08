# tests/test_registration.py

import pytest

from app import app


@pytest.fixture()
def client():
    app.config["WTF_CSRF_ENABLED"] = False  # disable CSRF for tests
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def valid_payload():
    return {
        "email": "test@example.com",
        "phone": 1234567890,   # 10 digits
        "name": "John Doe",
        "address": "123 Main St",
        "index": 1000,
        "comment": "No comments",
    }


def test_registration_success(client):
    response = client.post("/registration", json=valid_payload())
    assert response.status_code == 201
    assert response.get_json() == {"message": "Registration successful!"}


def test_registration_missing_email(client):
    payload = valid_payload()
    del payload["email"]
    response = client.post("/registration", json=payload)
    errors = response.get_json()["errors"]
    assert response.status_code == 400
    assert "email" in errors


def test_registration_invalid_email(client):
    payload = valid_payload()
    payload["email"] = "invalid-email"
    response = client.post("/registration", json=payload)
    errors = response.get_json()["errors"]
    assert response.status_code == 400
    assert "email" in errors


def test_registration_phone_too_short(client):
    payload = valid_payload()
    payload["phone"] = 12345  # too short
    response = client.post("/registration", json=payload)
    errors = response.get_json()["errors"]
    assert response.status_code == 400
    assert "phone" in errors


def test_registration_negative_phone(client):
    payload = valid_payload()
    payload["phone"] = -1234567890
    response = client.post("/registration", json=payload)
    errors = response.get_json()["errors"]
    assert response.status_code == 400
    assert "phone" in errors


def test_registration_missing_name(client):
    payload = valid_payload()
    del payload["name"]
    response = client.post("/registration", json=payload)
    errors = response.get_json()["errors"]
    assert response.status_code == 400
    assert "name" in errors


def test_registration_missing_address(client):
    payload = valid_payload()
    del payload["address"]
    response = client.post("/registration", json=payload)
    errors = response.get_json()["errors"]
    assert response.status_code == 400
    assert "address" in errors


def test_registration_missing_index(client):
    payload = valid_payload()
    del payload["index"]
    response = client.post("/registration", json=payload)
    errors = response.get_json()["errors"]
    assert response.status_code == 400
    assert "index" in errors


def test_registration_index_not_number(client):
    payload = valid_payload()
    payload["index"] = "abc"  # not numeric
    response = client.post("/registration", json=payload)
    errors = response.get_json()["errors"]
    assert response.status_code == 400
    assert "index" in errors
