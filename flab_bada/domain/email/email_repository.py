from flab_bada.database.database import RedisConn
from flab_bada.domain import AbstractRepository


class EmailRedisRepository:
    def __init__(self):
        self.redis = RedisConn().get_session()

    def set_email_secret_data(self, email: str, secret_num: str) -> None:
        self.redis.set(email, secret_num)

    def get_email_secret_data(self, email: str) -> str:
        data = self.redis.get(email)

        if data is not None:
            data = data.decode("utf-8")
        else:
            data = ""

        return data


class FakeEmailRedisRepository(AbstractRepository):
    def __init__(self):
        self.email_secret_data = dict()

    def set_email_secret_data(self, email: str, secret_num: str) -> None:
        self.email_secret_data[email] = secret_num

    def get_email_secret_data(self, email) -> str:
        return self.email_secret_data.get(email)
