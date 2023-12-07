from io import BytesIO
from urllib import parse

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status

from gestao.web.api.document.utils import generate_report_users_file


def test_generate_report_users_file_correct() -> None:
    file_stream = generate_report_users_file([], [])
    assert isinstance(file_stream, BytesIO)


def test_generate_report_users_file_incorrect() -> None:
    try:
        file_stream = generate_report_users_file(1, 2)
    except Exception as e:
        assert isinstance(e, TypeError)


@pytest.mark.anyio
async def test_get_report_users_NoFilter(
    client: AsyncClient, fastapi_app: FastAPI
) -> None:
    url = fastapi_app.url_path_for("get_report_users")
    response = await client.get(url)
    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_report_users_Filter(
    client: AsyncClient, fastapi_app: FastAPI
) -> None:
    url = fastapi_app.url_path_for("get_report_users")
    filter = ["fullName", "registration", "bloodType"]
    url += "?" + parse.urlencode({"filter_list": filter})
    response = await client.get(url)
    assert response.status_code == 200
