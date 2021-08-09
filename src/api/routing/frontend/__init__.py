from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="src/web/templates")


@router.get("/login/")
async def get_login(request: Request):
    return templates.TemplateResponse("login/login.html", {"request": request})


@router.post("/login/")
async def post_login(request: Request, username: str = Form(...)):
    pass
