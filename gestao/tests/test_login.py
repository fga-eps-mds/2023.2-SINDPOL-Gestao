import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status

from gestao.db.models.user import User
from gestao.tests.utils import generate_fake_user
from gestao.web.api.login.utils import generate_password, send_email


def test_generate_password_correct() -> None:
    password = generate_password()
    assert isinstance(password, str)
    assert len(password) == 8
    length = 15
    password = generate_password(length)
    assert isinstance(password, str)
    assert len(password) == 15


def test_generate_password_incorrect() -> None:
    try:
        generate_password("5")
    except Exception as e:
        assert isinstance(e, TypeError)


def test_send_email_incorrect() -> None:
    send_email_value = None
    try:
        send_email_value = send_email(
            user_name="joao",
            user_email="joao@example.com",
            new_password="null",
            logo_path="null",
        )
    except Exception as e:
        assert send_email_value is None


@pytest.mark.anyio
async def test_login_user_correct(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("create_user")
    user = generate_fake_user()
    response = await client.post(url, json=user)
    assert response.status_code == 200
    user_data = response.json()
    user_instance = User(**user_data)
    assert isinstance(user_instance, User)
    user_credentials = {
        "registration": user_data["registration"],
        "password": user_data["password"],
    }

    url = fastapi_app.url_path_for("login_user")
    response = await client.post(url, json=user_credentials)
    assert response.status_code == 200


@pytest.mark.anyio
async def test_login_user_incorrect(client: AsyncClient, fastapi_app: FastAPI) -> None:
    user_credentials = {
        "registration": "email@example.com",
        "password": "password_example",
    }

    url = fastapi_app.url_path_for("login_user")
    response = await client.post(url, json=user_credentials)
    assert response.status_code == 404


@pytest.mark.anyio
async def test_recover_password_UserNotFound(
    client: AsyncClient, fastapi_app: FastAPI
) -> None:
    user_credentials = {
        "email": "email@example.com",
    }

    url = fastapi_app.url_path_for("recover_password")
    response = await client.post(url, json=user_credentials)
    assert response.status_code == 400


@pytest.mark.anyio
async def test_recover_password_AuthenticationError(
    client: AsyncClient, fastapi_app: FastAPI
) -> None:
    url = fastapi_app.url_path_for("create_user")
    user = generate_fake_user()
    response = await client.post(url, json=user)
    assert response.status_code == 200
    user_data = response.json()
    user_instance = User(**user_data)
    assert isinstance(user_instance, User)

    user_credentials = {
        "email": user_data["email"],
    }

    url = fastapi_app.url_path_for("recover_password")
    response = await client.post(url, json=user_credentials)
    assert response.status_code == 400
