import os

from pydantic import BaseSettings


class TokenSetting(BaseSettings):
    SECRET_KEY = "flab"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    CONFIRM_TOKEN_EXPIRE_MINUTES = 3


class Dbconnection(BaseSettings):
    pass


class TestDbconnection(BaseSettings):
    db_user = "root"
    db_password = "dltjdrnr3137"
    db_host = "localhost"
    db_port = 3306
    db_name = "test"


class RedisConnection(BaseSettings):
    host = "localhost"
    port = 6379


def db_setting():
    if os.getenv("APP_ENV", "test") == "test":
        return TestDbconnection()
    return Dbconnection()


db_setting = db_setting()
token_setting = TokenSetting()
redist_setting = RedisConnection()
