import sys
import uuid
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.database import Base, get_db
from app.main import app
from app.models.user import User  # noqa: F401
from app.models.wardrobe_item import WardrobeItem  # noqa: F401


@pytest.fixture()
def client():
    temp_dir = Path(__file__).resolve().parent / ".tmp"
    temp_dir.mkdir(exist_ok=True)
    test_db_path = temp_dir / f"{uuid.uuid4().hex}.db"
    test_database_url = f"sqlite:///{test_db_path}"
    engine = create_engine(
        test_database_url,
        connect_args={"check_same_thread": False},
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)
    engine.dispose()
    test_db_path.unlink(missing_ok=True)


@pytest.fixture()
def user_payload():
    return {
        "email": "ioana@example.com",
        "password": "strong-password",
        "full_name": "Ioana Test",
    }


@pytest.fixture()
def auth_headers(client, user_payload):
    client.post("/auth/register", json=user_payload)
    response = client.post(
        "/auth/login",
        data={
            "username": user_payload["email"],
            "password": user_payload["password"],
        },
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
