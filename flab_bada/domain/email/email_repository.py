from flab_bada.database.database import get_redis_db
from flab_bada.domain import AbstractRepository
from fastapi import Depends
from redis import Redis


class EmailRedisRepository(AbstractRepository):
    def __init__(self, redis_data: Redis = Depends(get_redis_db)):
        self.redis = redis_data

    def set_email_secret_data(self, email: str, secret_num: str) -> None:
        self.redis.set(email, secret_num)

    def get_email_secret_data(self, email: str) -> str:
        data = self.redis.get(email)

        if not data:
            return ""
        return data.decode("utf-8")


class FakeEmailRedisRepository(AbstractRepository):
    def __init__(self):
        self.email_secret_data = dict()

    def set_email_secret_data(self, email: str, secret_num: str) -> None:
        self.email_secret_data[email] = secret_num

    def get_email_secret_data(self, email) -> str:
        return self.email_secret_data.get(email)
