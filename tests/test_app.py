import pytest
from app import app, members


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client

    members.clear()


def test_home_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "running"


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_get_members_returns_empty_list(client):
    response = client.get("/members")

    assert response.status_code == 200
    assert response.json == []


def test_add_member_successfully(client):
    response = client.post(
        "/members",
        json={"name": "Chaitanya", "plan": "Premium"}
    )

    assert response.status_code == 201
    assert response.json["name"] == "Chaitanya"
    assert response.json["plan"] == "Premium"
    assert response.json["id"] == 1


def test_add_member_without_name(client):
    response = client.post(
        "/members",
        json={"plan": "Premium"}
    )

    assert response.status_code == 400
    assert response.json["error"] == "Member name is required"


def test_add_member_without_plan(client):
    response = client.post(
        "/members",
        json={"name": "Chaitanya"}
    )

    assert response.status_code == 400
    assert response.json["error"] == "Membership plan is required"


def test_add_member_without_json(client):
    response = client.post("/members")

    assert response.status_code == 400
    assert response.json["error"] == "A JSON object is required"