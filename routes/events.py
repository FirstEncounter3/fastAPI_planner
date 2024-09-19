from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status
from database.connection import Database


from models.events import Event, EventUpdate

event_database = Database(Event)


event_router = APIRouter(
    tags=["Events"],
)


@event_router.get("/", response_model=list[Event])
async def retrieve_all_events() -> list[Event]:
    events = await event_database.get_all()
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )

    return event


@event_router.post("/new")
async def create_event(body: Event) -> dict:
    await event_database.save(body)
    return {"message": "Event created successfully"}


@event_router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate) -> Event:
    updateed_event = await event_database.update(id, body)
    if not updateed_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )

    return updateed_event


@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    deleted_event = await event_database.delete(id)
    if not deleted_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )

    return {"message": "Event deleted successfully"}


# experimental
@event_router.delete("/")
async def delete_all_events() -> dict:
    await event_database.delete_all()
    return {"message": "All events deleted successfully"}
