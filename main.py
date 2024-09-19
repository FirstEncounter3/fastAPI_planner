from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routes.users import user_router
from routes.events import event_router

from database.connection import Settings

import uvicorn

settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await settings.initialize_database()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.get("/")
async def home():
    return RedirectResponse(url="/event")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)