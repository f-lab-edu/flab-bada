from fastapi import APIRouter, status
from flab_bada.schemas.users import BaseUser

controller_router = APIRouter()


@controller_router.get("/")
async def say_controller() -> dict:
    return {"message": "Hello! Controller"}
