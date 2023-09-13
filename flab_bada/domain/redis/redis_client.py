from flab_bada.database.database import get_redis_db
from flab_bada.domain import AbstractRepository
from fastapi import Depends
from redis import Redis


class RedisClient(AbstractRepository):
    def __init__(self, redis_client: Redis = Depends(get_redis_db)):
        self.redis_client = redis_client

    def set(self, name: str, value: str):
        self.redis_client.set(name=name, value=value)

    def get(self, name: str) -> str:
        data = self.redis_client.get(name=name)

        if data != "":
            data = data.decode("utf-8")

        return data


class FakeRedisClient(AbstractRepository):
    def __init__(self):
        self.data = dict()

    def set(self, name: str, value: str):
        self.data[name] = value

    def get(self, name: str):
        return self.data.get(name, "")
