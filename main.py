from fastapi import FastAPI
from flab_bada.controller.controller import controller_router
from flab_bada.domain.users.user_controller import user_router


app = FastAPI()
app.include_router(controller_router)
app.include_router(user_router)
