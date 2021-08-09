from time import time

from fastapi import APIRouter, Request, Response
from pydantic import BaseModel


class MessageRequest(BaseModel):
    message: str


class Message(BaseModel):
    id: int
    author: str
    message: str


messages = []

router = APIRouter(prefix="/api")

@router.get("/messages")
async def get_recent_messages() -> list[Message]:
    return messages

@router.post("/messages")
async def post_message(message: MessageRequest, request: Request) -> Response:
    if not (username := request.cookies.get("username")):
        return Response(status_code=400)

    messages.append({
        "message": message.message,
        "author": username,
        "id": round(time() * 1000)
    })

    if len(messages) > 50:
        messages.pop(0)

    return Response(status_code=200)
