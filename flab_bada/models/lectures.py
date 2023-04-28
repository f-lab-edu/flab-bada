from . import Column, Integer, String
from . import Base


class Lecture(Base):
    __tablename__: str = "lectures"

