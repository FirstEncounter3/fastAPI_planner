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


class TokenResponse(BaseModel):
    access_token: str
    token_type: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": [
                {
                    "access_token": "eyJhbGciOiJIUz4.eyJzdWIiOiJhZG1pbiIsIm5pY2tObyI6IjIzMDUifQ.eyJpYXQiOjE2NjUzNjUyNjAsImV4cCI6MTY2NTM2OTI2NjAxfQ",
                    "token_type": "Bearer",
                }
            ]
        }
    )
