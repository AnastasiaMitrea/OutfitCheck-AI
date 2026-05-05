def test_register_creates_user(client, user_payload):
    response = client.post("/auth/register", json=user_payload)

    assert response.status_code == 200
    data = response.json()
    assert data["email"] == user_payload["email"]
    assert data["full_name"] == user_payload["full_name"]
    assert "id" in data
    assert "created_at" in data
    assert "password" not in data
    assert "hashed_password" not in data


def test_duplicate_registration_is_rejected(client, user_payload):
    first_response = client.post("/auth/register", json=user_payload)
    duplicate_response = client.post("/auth/register", json=user_payload)

    assert first_response.status_code == 200
    assert duplicate_response.status_code == 400
    assert duplicate_response.json()["detail"] == "Email already registered"


def test_login_returns_access_token(client, user_payload):
    client.post("/auth/register", json=user_payload)

    response = client.post(
        "/auth/login",
        data={
            "username": user_payload["email"],
            "password": user_payload["password"],
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["access_token"]
    assert data["token_type"] == "bearer"


def test_me_works_with_valid_bearer_token(client, user_payload, auth_headers):
    response = client.get("/auth/me", headers=auth_headers)

    assert response.status_code == 200
    data = response.json()
    assert data["email"] == user_payload["email"]
    assert data["full_name"] == user_payload["full_name"]


def test_me_fails_without_token(client):
    response = client.get("/auth/me")

    assert response.status_code == 401
