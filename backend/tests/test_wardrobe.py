import pytest


@pytest.fixture()
def item_payload():
    return {
        "image_url": "local://wardrobe/black-shirt.jpg",
        "category": "top",
        "color": "black",
        "style": "casual",
        "season": "spring",
        "tags": "shirt,cotton",
    }


def test_create_wardrobe_item_works_with_token(client, auth_headers, item_payload):
    response = client.post("/wardrobe/items", json=item_payload, headers=auth_headers)

    assert response.status_code == 201
    data = response.json()
    assert data["image_url"] == item_payload["image_url"]
    assert data["category"] == item_payload["category"]
    assert data["user_id"]
    assert "id" in data
    assert "created_at" in data


def test_get_wardrobe_items_returns_current_users_items(client, auth_headers, item_payload):
    client.post("/wardrobe/items", json=item_payload, headers=auth_headers)

    response = client.get("/wardrobe/items", headers=auth_headers)

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["image_url"] == item_payload["image_url"]


def test_get_wardrobe_item_by_id_works_for_owner(client, auth_headers, item_payload):
    create_response = client.post("/wardrobe/items", json=item_payload, headers=auth_headers)
    item_id = create_response.json()["id"]

    response = client.get(f"/wardrobe/items/{item_id}", headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["id"] == item_id


def test_update_wardrobe_item_updates_item(client, auth_headers, item_payload):
    create_response = client.post("/wardrobe/items", json=item_payload, headers=auth_headers)
    item_id = create_response.json()["id"]

    response = client.put(
        f"/wardrobe/items/{item_id}",
        json={"color": "white", "season": "summer"},
        headers=auth_headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["color"] == "white"
    assert data["season"] == "summer"
    assert data["category"] == item_payload["category"]


def test_delete_wardrobe_item_deletes_item(client, auth_headers, item_payload):
    create_response = client.post("/wardrobe/items", json=item_payload, headers=auth_headers)
    item_id = create_response.json()["id"]

    delete_response = client.delete(f"/wardrobe/items/{item_id}", headers=auth_headers)
    get_response = client.get(f"/wardrobe/items/{item_id}", headers=auth_headers)

    assert delete_response.status_code == 204
    assert delete_response.content == b""
    assert get_response.status_code == 404


@pytest.mark.parametrize(
    ("method", "path"),
    [
        ("post", "/wardrobe/items"),
        ("get", "/wardrobe/items"),
        ("get", "/wardrobe/items/1"),
        ("put", "/wardrobe/items/1"),
        ("delete", "/wardrobe/items/1"),
    ],
)
def test_wardrobe_endpoints_fail_without_token(client, item_payload, method, path):
    request = getattr(client, method)
    kwargs = {}
    if method in {"post", "put"}:
        kwargs["json"] = item_payload

    response = request(path, **kwargs)

    assert response.status_code == 401
