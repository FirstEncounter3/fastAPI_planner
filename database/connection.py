from beanie import PydanticObjectId, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from pydantic import ConfigDict, BaseModel
from pydantic_settings import BaseSettings

from models.users import User
from models.events import Event


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    SECRET_KEY: Optional[str] = "SECRET_KEY"

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(
            database=client.get_default_database(),
            document_models=[Event, User],
        )

    model_config = ConfigDict(env_file=".env")


class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()
        return

    async def get(self, id: PydanticObjectId) -> any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> list[any]:
        docs = await self.model.find_all().to_list()
        return docs

    async def update(self, id: PydanticObjectId, body: BaseModel) -> any:
        doc_id = id
        des_body = body.model_dump()
        des_body = {k: v for k, v in des_body.items() if v is not None}
        update_query = {"$set": {field: value for field, value in des_body.items()}}
        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc

    async def delete(self, id: PydanticObjectId) -> any:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True

    # experimental
    async def delete_all(self) -> any:
        docs = await self.get_all()
        for doc in docs:
            await doc.delete()
        return True
