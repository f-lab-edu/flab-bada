from fastapi import Depends
from sqlalchemy.orm import Session
from flab_bada.models.lectures import Lecture
from flab_bada.database.database import get_db


class LectureRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_lectures(self, lecture: Lecture) -> Lecture:
        """강의 등록"""
        self.db.add(lecture)
        self.db.commit()
        self.db.refresh(lecture)
        return lecture

    def get_total_lectures(self, lecture: Lecture):
        lectures_data = self.db.query(lecture).all()
        return lectures_data
