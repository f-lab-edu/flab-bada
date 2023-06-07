from fastapi import Depends
from .lectures_repository import LectureRepository
from flab_bada.schemas.lectures import CreateLecture
from flab_bada.models.lectures import Lecture


class LecturesService:
    def __init__(self, lecture_repository: LectureRepository = Depends()):
        self.lecture_repository = lecture_repository

    def create_lecture(self, create_lecture: CreateLecture):
        """강의 생성"""

        # 선생님인지 확인이 필요하다.

        # 강의 생성
        lecture = self.lecture_repository.create_lectures(
            lecture=Lecture(
                user_id=create_lecture.user_id,
                name=create_lecture.name,
                doc=create_lecture.doc,
            )
        )
        return lecture
