"""
    User 로직

    1. 유저 조회
    2. 유저 생성
    3. 유저 삭제
    4. 로그인 토큰 생성
    5. 메일 인증 로직
        (1) 메일 여러번 클릭 했을 경우
"""
from flab_bada.domain.users.user_repository import UserRepository
from flab_bada.models.users import User
from flab_bada.schemas.users import BaseUser
from sqlalchemy.orm import Session
from flab_bada.loggin.loggin import log_config
from flab_bada.utils.bcrypt import verify_password, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from fastapi import HTTPException, status
from datetime import timedelta


log = log_config("user service")


class UserService:
    def __init__(self, email: str, pw: str = ""):
        self.email = email
        self.pw = pw
        self._user_repository: UserRepository = UserRepository(email, pw)

    # 유저 조회
    def get_user(self, db: Session) -> User:
        """유저 조회

        Args:
             db: 디비
        Return:
            User: 유저 데이터
        """
        return self._user_repository.get_user(db)

    # 유저 생성
    def create_user(self, db: Session) -> dict:
        """유저 생성
        Args:
             db:
        Return:
            응답데이터 생성
        """

        # 중복 체크
        user = self.get_user(db=db)
        print(f"user: {user}")

        if not user:
            self._user_repository.create_user_data(
                db=db, user=User(email=self.email, password=self.pw)
            )
        else:
            return {
                "message": "중복 데이터가 존재합니다.",
                "status": "duplication"
            }

        return {
            "message": "저장을 완료 하였습니다.",
            "status": "ok"
        }

    # 이메일, 패스워드 체크
    def chk_email_password_user(self, db: Session) -> bool:
        """이메일, 패스워드 체크
        Args:
            db: 디비
        Return
            로그인 확인 True, 로그인 실패 False
        """
        chk_bool = False
        user: User = self.get_user(db)
        # 유저가 존재 한다면 입력 비번과 디비 정보 비번 비교
        if user:
            chk = verify_password(self.pw, user.password)
            if chk:
                chk_bool = True
        return chk_bool

    # 로그인
    def login(self, db: Session):
        """로그인을 한다.
        Args:
            db: 디비
        Return:
            dict: access token, token type
        """
        log.debug(" login start ")
        chk = self.chk_email_password_user(db)

        # 유저가 존재 한다면 입력 비번과 디비 정보 비번 비교
        if chk:
            # token 생성
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(
                data={"sub": self.email}, expires_delta=access_token_expires
            )
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="아이디와 비번이 틀렸습니다.")

        return {"access_token": access_token, "token_type": "bearer"}

    # 내정보
    def me(self, db: Session) -> BaseUser:
        """
            내 정보 데이터
        Args:
             db: 디비
        Return:
            BaseUser: 유저 데이터
        """
        user = self.get_user(db)
        return BaseUser(id=user.id, email=user.email)
