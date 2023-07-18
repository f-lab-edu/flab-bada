from fastapi import Depends
from sqlalchemy.orm import Session
from flab_bada.domain import AbstractRepository
from flab_bada.models.lectures import Lecture
from flab_bada.database.database import get_db
from flab_bada.schemas.lectures import CreateLecture
from typing import List
from flab_bada.logging.logging import log_config


log = log_config("lecture repository")


class LectureRepository(AbstractRepository):
    db: Session

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_user(self, user_id: int, role: str) -> Lecture | None:
        """유저 조회"""
        user = self.db.query(Lecture).filter(Lecture.user_id == user_id, Lecture.role == role).first()
        if not user:
            return None
        return user

    # 강의 등록
    def create_lectures(self, create_lecture: CreateLecture) -> CreateLecture:
        """강의 등록"""
        self.db.add(Lecture(**create_lecture.dict()))
        self.db.commit()
        self.db.refresh(create_lecture)
        return create_lecture

    # 강의 조회
    def get_lecture(self, lecture_id: int) -> Lecture | None:
        """강의 조회"""
        lecture = self.db.query(Lecture).filter(Lecture.id == lecture_id).first()
        return lecture

    # 등록된 강의 조회
    def get_lectures_by_teacher(self, teacher_id: int) -> Lecture:
        lectures = self.db.query(Lecture).filter(Lecture.user_id == teacher_id).all()
        return lectures

    # 강의 수정
    def update_lecture(self, teacher_id: int, lecture_id: int, update_data: dict) -> Lecture:
        lecture = self.db.query(Lecture).filter(Lecture.id == lecture_id, Lecture.user_id == teacher_id).one_or_none()

        # 데이터 존재 한다.
        if lecture:
            lecture.update(update_data)
            self.db.commit()
            self.db.refresh(lecture)
        return lecture

    # 강의 삭제
    def delete_lecture(self, lecture_id: int) -> None:
        pass


class FakeLectureRepository(AbstractRepository):
    def __init__(self) -> None:
        self.users = set()

    # 유저 조회
    def get_user(self, user_id: int, role: str) -> Lecture | None:
        for user in self.users:
            inner_user_id = user.user_id
            if inner_user_id == user_id and role == "teacher":
                return user
        return None

    # 강의 생성
    def create_lectures(self, create_lecture: CreateLecture) -> None:
        id_count = len(self.users) + 1
        self.users.add(
            Lecture(id=id_count, user_id=create_lecture.user_id, name=create_lecture.name, doc=create_lecture.doc)
        )

    # 강의 조회힌다.
    def get_lecture(self, lecture_id: int) -> Lecture | None:
        """강의 조회"""
        for lecture in self.users:
            inner_lecture_id = lecture.id
            if inner_lecture_id == lecture_id:
                return lecture
        return None

    # 등록된 강의 조회
    def get_lectures_by_teacher(self, teacher_id: int) -> List[Lecture]:
        """등록된 강의 조회"""
        log.info("get_lectures_by_teacher")
        lectures = []
        for lecture in self.users:
            inner_teacher_id = lecture.user_id
            if inner_teacher_id == teacher_id:
                lectures.append(lecture)

        log.info(f"lectures: {lectures}")
        return lectures

    # 강의 수정
    def update_lecture(self, teacher_id: int, lecture_id: int, update_data: dict) -> Lecture:
        """강의 수정"""
        for lecture in self.users:
            inner_lecture_id = lecture.id
            inner_teacher_id = lecture.user_id
            if inner_lecture_id == lecture_id and inner_teacher_id == teacher_id:
                lecture.name = update_data["name"]
                lecture.doc = update_data["doc"]
                return lecture

    # 강의 삭제
    def delete_lecture(self, lecture_id: int) -> None:
        self.users.remove(lecture_id)
