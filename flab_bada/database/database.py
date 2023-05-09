from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config.config import db_setting

# 환경 설정으로 옮겨야 한다.
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:dltjdrnr3137@localhost/nlp"
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{db_setting.db_user}:{db_setting.db_password}@{db_setting.db_host}/{db_setting.db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ConnDb:
    def __init__(self):
        self.db = next(get_db())

    def get_session(self):
        return self.db
