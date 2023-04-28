from . import Column, Integer, String
from . import Base


class User(Base):
    __tablename__: str = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String)
    password = Column(String)
    use_yn = Column(String, default="Y")
