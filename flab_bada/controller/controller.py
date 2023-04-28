from fastapi import APIRouter

controller_router = APIRouter()


@controller_router.get("/")
async def say_controller() -> dict:
    return {"message": "Hello! Controller"}
