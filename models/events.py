from pydantic import BaseModel


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: list[str]
    location: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "FastAPI book launch",
                    "image": "https://linktomyimg.com/img.png",
                    "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                    "tags": ["python", "fastapi", "book", "launch"],
                    "location": "San Francisco, CA",
                }
            ]
        }
    }
