import os

from pydantic import BaseSettings


class UrlSetting(BaseSettings):
    LOCAL_URL = "http://localhost:8000"


class TokenSetting(BaseSettings):
    SECRET_KEY = os.getenv("SECRET_KEY", "test")
    REFRESH_SECRET_KEY = os.getenv("REFRESH_SECRET_KEY", "test")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REFRESH_TOKEN_EXPIRE_MINUTES = 1440
    CONFIRM_TOKEN_EXPIRE_MINUTES = 3


class Dbconnection(BaseSettings):
    pass


class TestDbconnection(BaseSettings):
    db_user = os.getenv("DB_USER", "root")
    db_password = os.getenv("DB_PASSWORD", "dltjdrnr3137")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = 3306
    db_name = os.getenv("DB_NAME", "test")


class RedisConnection(BaseSettings):
    host = os.getenv("DB_HOST", "localhost")
    port = 6379


def db_setting():
    if os.getenv("APP_ENV", "test") == "test":
        return TestDbconnection()
    return Dbconnection()


db_setting = db_setting()
token_setting = TokenSetting()
redist_setting = RedisConnection()
url_setting = UrlSetting()
