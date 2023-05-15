from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flab_bada.database.database import Base
from .users import User


class Lecture(Base):
    __tablename__: str = "lectures"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    doc = Column(String)
    user = relationship(f"{User.__name__}")
