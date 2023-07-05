from sqlalchemy import Column, Integer, String
from flab_bada.database.database import Base


class User(Base):
    __tablename__: str = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String)
    password = Column(String)
    use_yn = Column(String, default="Y")
    role = Column(String, default="user")
