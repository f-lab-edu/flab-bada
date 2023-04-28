"""
    유저 데이터 베이스 저장 로직
    1. 유저 조회
    2. 유저 생성
"""
from flab_bada.schemas.users import CreateUser
from sqlalchemy.orm import Session
from flab_bada.models.users import User


class UserRepository:
    def __init__(self, email: str, pw: str = ""):
        self.email = email
        self.pw = pw

    def create_user_data(self, db: Session, user: CreateUser) -> None:
        """
            유저 생성
        Args:
            db: 디비
        """
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_user(self, db: Session):
        """
            유저 조회
        Args:
            db: 디비
        Return:
            유저 데이터
        """
        user = db.query(User).filter(User.email == self.email).first()
        if not user:
            return None
        return user
