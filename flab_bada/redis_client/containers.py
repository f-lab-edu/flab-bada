"""Containers module."""

from dependency_injector import containers, providers

from . import redis, services


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    redis_pool = providers.Resource(
        redis.init_redis_pool,
        host="localhost",
        port=6379,
    )

    service = providers.Factory(
        services.Service,
        redis_clinet=redis_pool,
    )
