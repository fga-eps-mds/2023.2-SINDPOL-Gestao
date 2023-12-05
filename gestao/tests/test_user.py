import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status
from uuid import uuid4

from gestao.db.models.user import User
from gestao.tests.utils import generate_fake_user


@pytest.mark.anyio
async def test_get_users(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("get_users")
    response = await client.get(url)
    assert response.status_code == 200
    user_data = response.json()
    assert isinstance(user_data, list)


@pytest.mark.anyio
async def test_get_user_correct(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("create_user")
    user = generate_fake_user()
    response = await client.post(url, json=user)
    assert response.status_code == 200
    user_data = response.json()
    user_id = user_data["id"]
    user_instance = User(**user_data)
    assert isinstance(user_instance, User)

    url = fastapi_app.url_path_for("get_user", user_id=user_id)
    response = await client.get(url)
    assert response.status_code == 200
    user_data = response.json()
    user_instance = User(**user_data)
    assert isinstance(user_instance, User)


@pytest.mark.anyio
async def test_get_user_incorrect(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("get_user", user_id=str(uuid4()))
    response = await client.get(url)
    assert response.status_code == 404


@pytest.mark.anyio
async def test_create_user_correct(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("create_user")
    user = generate_fake_user()
    response = await client.post(url, json=user)
    assert response.status_code == 200
    user_data = response.json()
    user_instance = User(**user_data)
    assert isinstance(user_instance, User)


@pytest.mark.anyio
async def test_create_user_incorrect(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("create_user")
    user = generate_fake_user()
    user.pop("fullName")
    response = await client.post(url, json=user)
    assert response.status_code == 422


@pytest.mark.anyio
async def test_create_user_UniqueViolation(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("create_user")
    user = generate_fake_user()
    response = await client.post(url, json=user)
    assert response.status_code == 200
    
    response = await client.post(url, json=user)
    assert response.status_code == 400


@pytest.mark.anyio
async def test_update_user_correct(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("create_user")
    user = generate_fake_user()
    response = await client.post(url, json=user)
    assert response.status_code == 200
    user_data = response.json()
    user_id = user_data["id"]
    user_instance = User(**user_data)
    assert isinstance(user_instance, User)

    url = fastapi_app.url_path_for("update_user", user_id=user_id)
    response = await client.put(
        url,
        json={
            "fullName": "pedro",
        },
    )
    assert response.status_code == 200
    user_data = response.json()
    user_instance = User(**user_data)
    assert isinstance(user_instance, User)


@pytest.mark.anyio
async def test_update_user_incorrect(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("update_user", user_id=str(uuid4()))
    response = await client.put(url, json={})
    assert response.status_code == 404


@pytest.mark.anyio
async def test_delete_user_correct(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("create_user")
    user = generate_fake_user()
    response = await client.post(url, json=user)
    assert response.status_code == 200
    user_data = response.json()
    user_id = user_data["id"]
    user_instance = User(**user_data)
    assert isinstance(user_instance, User)

    url = fastapi_app.url_path_for("delete_user", user_id=user_id)
    response = await client.delete(url)
    assert response.status_code == 200


@pytest.mark.anyio
async def test_delete_user_incorrect(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("delete_user", user_id=str(uuid4()))
    response = await client.delete(url)
    assert response.status_code == 200


@pytest.mark.anyio
async def test_disable_user_correct(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("create_user")
    user = generate_fake_user()
    response = await client.post(url, json=user)
    assert response.status_code == 200
    user_data = response.json()
    var = user_data["id"]
    user_instance = User(**user_data)
    assert isinstance(user_instance, User)

    url = fastapi_app.url_path_for("disable_user", user_id=var)
    response = await client.patch(url)
    assert response.status_code == 200


@pytest.mark.anyio
async def test_disable_user_incorrect(
    client: AsyncClient, fastapi_app: FastAPI
) -> None:
    url = fastapi_app.url_path_for("disable_user", user_id=str(uuid4()))
    response = await client.patch(url)
    assert response.status_code == 404


@pytest.mark.anyio
async def test_enable_user_correct(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("create_user")
    user = generate_fake_user()
    response = await client.post(url, json=user)
    assert response.status_code == 200
    user_data = response.json()
    var = user_data["id"]
    user_instance = User(**user_data)
    assert isinstance(user_instance, User)

    url = fastapi_app.url_path_for("enable_user", user_id=var)
    response = await client.patch(url)
    assert response.status_code == 200


@pytest.mark.anyio
async def test_enable_user_incorrect(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("enable_user", user_id=str(uuid4()))
    response = await client.patch(url)
    assert response.status_code == 404
