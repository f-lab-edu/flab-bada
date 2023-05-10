from fastapi import APIRouter


lectures = APIRouter(prefix="/v1/lectures")


@lectures.get("/")
def lectures():
    pass
