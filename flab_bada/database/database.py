from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from ..config.config import db_setting

# from aioredis import StrictRedis
import redis

# 환경 설정으로 옮겨야 한다.
SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{db_setting.db_user}:{db_setting.db_password}@{db_setting.db_host}/{db_setting.db_name}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_redis_db():
    host = "localhost"
    # password = ""
    port = 6379
    # session = from_url(f"redis://{host}", port=port, encoding="utf-8", decode_responses=True)
    session = redis.StrictRedis(host=host, port=port)
    try:
        yield session
    finally:
        session.close()


class ConnDb:
    def __init__(self):
        self.db = next(get_db())

    def get_session(self):
        return self.db


class RedisConn:
    def __init__(self):
        self.db = next(get_redis_db())

    def get_session(self):
        return self.db
