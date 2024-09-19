from sqlmodel import JSON, SQLModel, Field, Column
from pydantic import ConfigDict
from typing import Optional


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: list[str] = Field(sa_column=Column(JSON))
    location: str

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet",
            }
        },
    )


class EventUpdate(SQLModel):
    title: Optional[str] = Field(default=None)
    image: Optional[str] = Field(default=None)
    desctiption: Optional[str] = Field(default=None)
    tags: Optional[list[str]] = Field(default=None)
    location: Optional[str] = Field(default=None)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet",
            }
        }
    )
