from flab_bada.models.lectures import Lecture
from flab_bada.database.database import ConnDb


class LectureRepository:
    def __init__(self):
        self.db = ConnDb().get_session()

    def create_lectures(self, lecture: Lecture):
        """강의 등록"""
        self.db.commit()
        self.db.add(lecture)
        self.db.refresh(lecture)
        return lecture

    def get_total_lectures(self, lecture: Lecture):
        lectures_data = self.db.query(lecture).all()
        return lectures_data
