from typing import Type

from flab_bada.schemas.users import CreateUser
from flab_bada.models.users import User
from flab_bada.database.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from flab_bada.logging.logging import log_config
from .. import AbstractRepository

log = log_config("user repository")


class UserRepository(AbstractRepository):
    db: Session

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_user_data(self, user: CreateUser) -> CreateUser:
        """유저 생성
        Args:
            user:
        """
        log.debug(f" create_user_data -> data: {user}")
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user(self, email: str) -> Type[User] | None:
        """유저 조회
        Return:
            유저 데이터
        """
        user = self.db.query(User).filter(User.email == email).first()
        if not user:
            return None
        return user

    # 사용자에서 선생님으로 변경
    def change_role(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id)
        user.update({"role": "teacher"})
        self.db.commit()
        self.db.refresh(user)


class FakeUserRepository(AbstractRepository):
    def __init__(self):
        self.users = set()

    def create_user_data(self, user: CreateUser) -> CreateUser:
        """사용자 생성
        Args:
            user: 가입 유저 데이터
        Return:
            CreateUser: user
        """
        id_count = len(self.users)
        self.users.add(User(id=id_count, email=user.email, password=user.password, use_yn="N"))
        return user

    def get_user(self, email: str) -> Type[User] | None:
        for user in self.users:
            user_email = user.email
            if user_email == email:
                return user
        return None

    def change_role(self):
        pass
