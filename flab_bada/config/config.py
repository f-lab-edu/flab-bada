import os

from pydantic import BaseSettings


class TokenSetting(BaseSettings):
    SECRET_KEY = "flab"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Dbconnection(BaseSettings):
    pass


class TestDbconnection(BaseSettings):
    db_user = "admin"
    db_password = "dltjdrnr3137"
    db_host = "localhost"
    db_port = 3306
    db_name = "test"


def db_setting():
    if os.getenv("APP_ENV", "test") == "test":
        return TestDbconnection()
    return Dbconnection()


db_setting = db_setting()
