from fastapi import Depends
from sqlalchemy.orm import Session
from flab_bada.domain import AbstractRepository
from flab_bada.models.lectures import Lecture
from flab_bada.database.database import get_db
from flab_bada.schemas.lectures import CreateLecture


class LectureRepository(AbstractRepository):
    db: Session

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_user(self, user_id: int) -> Lecture | None:
        """유저 조회"""
        user = self.db.query(Lecture).filter(Lecture.user_id == user_id).first()
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

    # 강의 전체 조회
    def get_total_lectures(self, lecture: Lecture) -> list[Lecture]:
        """강의 전체 조회"""
        lectures_data = self.db.query(lecture).all()
        return lectures_data

    # 강의 수정
    def update_lecture(self, lecture_id: int, create_lecture: CreateLecture) -> Lecture:
        pass

    # 강의 삭제
    def delete_lecture(self, lecture_id: int) -> None:
        pass


class FakeLectureRepository(AbstractRepository):
    def __init__(self) -> None:
        self.users = set()

    # 유저 조회
    def get_user(self, user_id: int):
        for user in self.users:
            inner_user_id = user.user_id
            if inner_user_id == user_id:
                return user
        return None

    # 강의 생성
    def create_lectures(self, create_lecture: CreateLecture) -> None:
        id_count = len(self.users)
        self.users.add(Lecture(id=id_count, user_id=create_lecture.user_id, name=create_lecture.name, doc=create_lecture.doc))

    # 강의 전체 조회
    def get_total_lectures(self, lecture: Lecture) -> list[Lecture]:
        return list(self.users)

    # 강의 수정
    def update_lecture(self, lecture_id: int, create_lecture: CreateLecture) -> Lecture:
        pass

    # 강의 삭제
    def delete_lecture(self, lecture_id: int) -> None:
        self.users.remove(lecture_id)
