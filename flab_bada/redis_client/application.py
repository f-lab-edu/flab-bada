"""Application module."""

from dependency_injector.wiring import inject, Provide
from fastapi import Depends, APIRouter

from .containers import Container
from .services import Service

redis_router = APIRouter()


@redis_router.api_route("/")
@inject
async def index(service: Service = Depends(Provide[Container.service])):
    value = await service.process()
    return {"result": value}


container = Container()
# container.config.redis_host.from_env("REDIS_HOST", "localhost")
# container.config.redis_password.from_env("REDIS_PASSWORD", "password")
container.wire(modules=[__name__])
