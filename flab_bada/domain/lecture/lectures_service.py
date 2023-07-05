from fastapi import Depends
from .lectures_repository import LectureRepository
from flab_bada.schemas.lectures import CreateLecture
from flab_bada.models.lectures import Lecture


class LecturesService:
    def __init__(self, lecture_repository: LectureRepository = Depends()):
        self.lecture_repository = lecture_repository

    # 강의 등록
    def create_lecture(self, create_lecture: CreateLecture):
        """강의 생성"""

        # 선생님인지 확인이 필요하다.
        self.lecture_repository.get_user(create_lecture.user_id)

        # 강의 생성
        self.lecture_repository.create_lectures(create_lecture=create_lecture)

    # 강의 조회
    def get_lecture(self, lecture_id: int) -> Lecture:
        pass

    # 강의 수정
    def update_lecture(self, lecture_id: int, create_lecture: CreateLecture) -> Lecture:
        pass

    # 강의 삭제
    def delete_lecture(self, lecture_id: int) -> None:
        pass

    def get_user(self, user_id: int) -> Lecture:
        return self.lecture_repository.get_user(user_id=user_id)
