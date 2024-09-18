from pydantic import BaseModel, EmailStr
from typing import Optional
from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[list[Event]] = []

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "pQ8oG@example.com",
                    "password": "secret",
                    "events": [],
                }
            ]
        }
    }


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
