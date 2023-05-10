from typing import Annotated
from fastapi import APIRouter, Depends


controller_router = APIRouter()


@controller_router.get("/")
async def say_controller() -> dict:
    return {"message": "Hello! Controller"}


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@controller_router.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
