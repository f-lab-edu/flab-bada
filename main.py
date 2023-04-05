from fastapi import FastAPI
from flab_bada.controller.controller import controller_router

app = FastAPI()
app.include_router(controller_router)


@app.get("/")
async def helloworld() -> dict:
    return {"message": "hello world"}
