from typing import Coroutine

from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles

from .routing import router
from .utils import Redis


app = FastAPI(docs_url=None)
app.mount("/static", StaticFiles(directory="src/web/static"), "static")
app.include_router(router)

redis = Redis()


@app.on_event("startup")
async def on_startup() -> None:
    """Initialize the database and redis connections."""
    await redis.ainit()


@app.get("/")
async def test():
    return {"message": "something"}


@app.middleware("http")
async def attach(request: Request, call_next: Coroutine) -> Response:
    """Attach the databases and redis connections to requests."""

    request.state.redis = redis

    return await call_next(request)
