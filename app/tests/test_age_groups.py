import pytest
from bson import ObjectId
from fastapi.testclient import TestClient
from fastapi import status


def test_create_age_group_successfully(client: TestClient, valid_age_group: dict):
    response = client.post(
        "/api/v1/age-groups/", json=valid_age_group, auth=(pytest.admin_user, pytest.admin_password),
    )
    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()

    assert data["_id"] is not None
    assert data["minimum_age"] == valid_age_group["minimum_age"]
    assert data["maximum_age"] == valid_age_group["maximum_age"]

    new_age_group = pytest.collection.find_one({"_id": ObjectId(data["_id"])})

    assert new_age_group is not None


def test_cant_create_age_group_with_negative_age_group(client: TestClient):
    invalid_age_group = {"minimum_age": -1, "maximum_age": -100}
    response = client.post(
        "/api/v1/age-groups/", json=invalid_age_group, auth=(pytest.admin_user, pytest.admin_password),
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_cant_create_age_group_with_invalid_range(client: TestClient):
    invalid_age_group = {"minimum_age": 100, "maximum_age": 1}
    response = client.post(
        "/api/v1/age-groups/", json=invalid_age_group, auth=(pytest.admin_user, pytest.admin_password),
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_cant_create_duplicated_age_group(client: TestClient, age_group: dict):
    age_group.pop("_id")
    response = client.post(
        "/api/v1/age-groups/", json=age_group, auth=(pytest.admin_user, pytest.admin_password),
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_get_age_group_sucessfully(client: TestClient, age_group: dict):
    response = client.get(
        f"/api/v1/age-groups/{age_group['_id']}/", auth=(pytest.admin_user, pytest.admin_password),
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert isinstance(data, dict)
    assert data["_id"] == age_group["_id"]


def test_list_age_groups_sucessfully(client: TestClient, age_group: dict):
    response = client.get(
        "/api/v1/age-groups/", auth=(pytest.admin_user, pytest.admin_password),
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert isinstance(data, list)
    assert data[0]["_id"] == age_group["_id"]


def test_delete_age_groups_sucessfully(client: TestClient, age_group: dict):
    response = client.delete(
        f"/api/v1/age-groups/{age_group['_id']}/", auth=(pytest.admin_user, pytest.admin_password),
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT

    deleted_age_group = pytest.collection.find_one({"_id": ObjectId(age_group["_id"])})

    assert deleted_age_group is None
