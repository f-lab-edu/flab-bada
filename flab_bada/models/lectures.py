from sqlalchemy import Column, Integer, String, ForeignKey
from flab_bada.database.database import Base


class Lecture(Base):
    __tablename__: str = "lectures"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    doc = Column(String)

    # relation 관련
    # lecture = relationship("")
