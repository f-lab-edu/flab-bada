from fastapi import FastAPI
from flab_bada.controller.controller import controller_router
from flab_bada.domain.users.user_controller import user_router
from flab_bada.domain.email.email_controller import email_router


app = FastAPI()
app.include_router(controller_router)
app.include_router(user_router)
app.include_router(email_router)
