import pytest
import httpx

from httpx import ASGITransport

from main import app
from database.connection import Settings
from models.events import Event
from models.users import User


async def init_test_db():
    test_settings = Settings()
    test_settings.DATABASE_URL = "mongodb://localhost:27017/test"

    await test_settings.initialize_database()


@pytest.fixture
async def default_client():
    await init_test_db()
    async with httpx.AsyncClient(
        transport=ASGITransport(app=app), base_url="http://app"
    ) as client:
        yield client


@pytest.fixture
async def cleanup_db():
    yield
    await Event.find_all().delete()
    await User.find_all().delete()
