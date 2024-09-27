from typing import AsyncGenerator
import httpx
import pytest

from auth.jwt_handler import create_access_token
from models.events import Event

# cleanup_db_events: None


@pytest.fixture
async def access_token() -> str:
    return create_access_token({"user": "testuser@test.org"})


@pytest.fixture
async def mock_event() -> AsyncGenerator[Event, None]:
    new_event = Event(
        creator="testuser@test.org",
        title="Test Event",
        image="https://linktomyimage.com/image.png",
        description="Test description",
        tags=["tag1", "tag2"],
        location="Test location",
    )

    await Event.insert_one(new_event)

    yield new_event


@pytest.mark.asyncio
async def test_get_events(default_client: httpx.AsyncClient, mock_event: Event) -> None:
    response = await default_client.get("/event/")

    assert response.status_code == 200
    assert response.json()[0]["_id"] == str(mock_event.id)


@pytest.mark.asyncio
async def test_get_event(default_client: httpx.AsyncClient, mock_event: Event) -> None:
    url = f"event/{str(mock_event.id)}"
    response = await default_client.get(url)

    assert response.status_code == 200
    assert response.json()["creator"] == mock_event.creator
    assert response.json()["_id"] == str(mock_event.id)


@pytest.mark.asyncio
async def test_post_event(default_client: httpx.AsyncClient, access_token: str) -> None:
    payload = {
        "title": "Test Event",
        "image": "https://linktomyimage.com/image.png",
        "description": "Test description",
        "tags": ["tag1", "tag2"],
        "location": "Test location",
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    test_response = {
        "message": "Event created successfully",
    }

    response = await default_client.post("/event/new", json=payload, headers=headers)

    assert response.status_code == 200
    assert response.json() == test_response


@pytest.mark.asyncio
async def test_get_events_count(
    default_client: httpx.AsyncClient, cleanup_db_events: None
) -> None:
    response = await default_client.get("/event/")
    events = response.json()

    assert response.status_code == 200
    assert len(events) == 3


@pytest.mark.asyncio
async def test_update_event(
    default_client: httpx.AsyncClient,
    mock_event: Event,
    access_token: str,
    cleanup_db_events: None,
) -> None:
    test_payload = {
        "title": "Updated test Event",
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    url = f"event/{str(mock_event.id)}"

    response = await default_client.put(url, json=test_payload, headers=headers)

    assert response.status_code == 200
    assert response.json()["title"] == test_payload["title"]


@pytest.mark.asyncio
async def test_delete_event(
    default_client: httpx.AsyncClient, mock_event: Event, access_token: str
) -> None:
    test_response = {
        "message": "Event deleted successfully",
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    url = f"event/{str(mock_event.id)}"

    response = await default_client.delete(url, headers=headers)

    assert response.status_code == 200
    assert response.json() == test_response
