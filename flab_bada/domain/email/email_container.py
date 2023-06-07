from dependency_injector import containers, providers
from flab_bada.database.database import get_redis_db
from flab_bada.domain.email.email_service import EmailService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    redis_pool = providers.Resource(
        get_redis_db,
    )

    service = providers.Factory(
        EmailService,
        redis=redis_pool,
    )
