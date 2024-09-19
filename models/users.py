from pydantic import BaseModel, EmailStr, ConfigDict
from beanie import Document, Link
from typing import Optional

from models.events import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[list[Link[Event]]] = []

    class Settings:
        name = "users"

    model_config = ConfigDict(
        json_schema_extra={
            "example": [
                {
                    "email": "pQ8oG@example.com",
                    "password": "secret",
                    "events": [],
                }
            ]
        }
    )


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "pQ8oG@example.com",
                    "password": "secret",
                }
            ]
        }
    }
