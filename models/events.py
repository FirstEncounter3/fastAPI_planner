from beanie import Document
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class Event(Document):
    title: str
    image: str
    description: str
    tags: list[str]
    location: str
    creator: Optional[str] = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "FastAPI book launch",
                "image": "https://linktomyimg.com/img.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "San Francisco, CA"
            }
        }
    )

    class Settings:
        name = "events"


class EventUpdate(BaseModel):
    title: Optional[str] = Field(default=None)
    image: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    tags: Optional[list[str]] = Field(default=None)
    location: Optional[str] = Field(default=None)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
    )
