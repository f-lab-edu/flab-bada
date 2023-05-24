"""
    유저 데이터 베이스 저장 로직
    1. 유저 조회
    2. 유저 생성
"""
from typing import Type

from flab_bada.schemas.users import CreateUser
from flab_bada.models.users import User
from flab_bada.database.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from flab_bada.loggin.loggin import log_config
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
