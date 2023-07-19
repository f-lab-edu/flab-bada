from typing import List
from fastapi import Depends
from .lectures_repository import LectureRepository
from flab_bada.schemas.lectures import CreateLecture, ReturnLecture
from flab_bada.models.lectures import Lecture


class LecturesService:
    def __init__(self, lecture_repository: LectureRepository = Depends()):
        self.lecture_repository = lecture_repository

    # 강사 조회
    def get_user(self, user_id: int, role: str) -> Lecture:
        return self.lecture_repository.get_user(user_id=user_id, role=role)

    # 강의 등록
    def create_lecture(self, create_lecture: CreateLecture):
        """강의 생성"""

        # 선생님인지 확인이 필요하다. (고민 로그인 후 선생님롤이면 화면이 변경 되지 않을까?)
        # self.lecture_repository.get_user(create_lecture.user_id, create_lecture.role)

        # 강의 생성
        self.lecture_repository.create_lectures(create_lecture=create_lecture)

    # 강의 조회
    def get_lecture(self, lecture_id: int) -> ReturnLecture | dict:
        """강의 조회"""
        lecture = self.lecture_repository.get_lecture(lecture_id=lecture_id)

        if lecture:
            return ReturnLecture(id=lecture.id, user_id=lecture.user_id, name=lecture.name, doc=lecture.doc)
        else:
            return {"message": "강의가 존재하지 않습니다."}

    # 등록된 강의 조회
    def get_lectures_by_teacher(self, teacher_id: int) -> List[ReturnLecture]:
        """등록된 강의 조회"""
        lectures = self.lecture_repository.get_lectures_by_teacher(teacher_id)

        if len(lectures):
            return [
                ReturnLecture(id=lecture.id, user_id=lecture.user_id, name=lecture.name, doc=lecture.doc)
                for lecture in lectures
            ]
        else:
            return {"message": "강의가 존재하지 않습니다."}

    # 강의 수정
    def update_lecture(self, tearcher_id: int, lecture_id: int, update_data: dict):
        """강의 수정"""
        self.lecture_repository.update_lecture(teacher_id=tearcher_id, lecture_id=lecture_id, update_data=update_data)

    # 강의 삭제
    def delete_lecture(self, lecture_id: int) -> None:
        """강의 삭제"""
        self.lecture_repository.delete_lecture(lecture_id=lecture_id)
