from typing import Any, AsyncGenerator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.engine import create_engine

from gestao.db.config import database
from gestao.db.utils import create_database, drop_database
from gestao.settings import settings
from gestao.web.application import get_app


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    """
    Backend for anyio pytest plugin.

    :return: backend name.
    """
    return "asyncio"


@pytest.fixture(autouse=True)
async def initialize_db() -> AsyncGenerator[None, None]:
    """
    Create models and databases.

    :yield: new engine.
    """
    from gestao.db.meta import meta  # noqa: WPS433
    from gestao.db.models import load_all_models  # noqa: WPS433

    load_all_models()

    create_database()

    engine = create_engine(str(settings.db_url))
    with engine.begin() as conn:
        meta.create_all(conn)

    engine.dispose()

    await database.connect()

    yield

    await database.disconnect()
    drop_database()


@pytest.fixture
def fastapi_app() -> FastAPI:
    """
    Fixture for creating FastAPI app.

    :return: fastapi app with mocked dependencies.
    """
    application = get_app()
    return application  # noqa: WPS331


@pytest.fixture
async def client(
    fastapi_app: FastAPI,
    anyio_backend: Any,
) -> AsyncGenerator[AsyncClient, None]:
    """
    Fixture that creates client for requesting server.

    :param fastapi_app: the application.
    :yield: client for the app.
    """
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac
