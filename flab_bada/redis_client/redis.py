from typing import AsyncIterator

from aioredis import from_url, Redis


async def init_redis_pool(host: str, port: int) -> AsyncIterator[Redis]:
    # session = from_url(f"redis://{host}")
    session = from_url("redis://localhost")
    yield session
    session.close()
    await session.wait_closed()
