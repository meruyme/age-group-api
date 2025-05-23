import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core.db import DatabaseProvider


def pytest_configure():
    pytest.db = DatabaseProvider.get_database()
    pytest.collection = pytest.db.age_groups
    pytest.admin_user = "admin_user"
    pytest.admin_password = "admin"


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def setup_test_database(monkeypatch):
    def database():
        return pytest.db

    monkeypatch.setattr(
        DatabaseProvider,
        "get_database",
        database,
    )

    db = pytest.db
    db.drop_collection("age_groups")
    yield
    db.drop_collection("age_groups")


@pytest.fixture
def valid_age_group():
    return {"minimum_age": 0, "maximum_age": 100}


@pytest.fixture
def age_group():
    age_group = pytest.collection.insert_one({
        "minimum_age": 0,
        "maximum_age": 100,
    })

    return {
        "_id": str(age_group.inserted_id),
        "minimum_age": 0,
        "maximum_age": 100,
    }
