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
from flab_bada.schemas.users import BaseUser, CreateUser
from flab_bada.logging.logging import log_config
from flab_bada.utils.bcrypt import (
    verify_password,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    get_cryptcontext,
)
from fastapi import HTTPException, status, Depends
from datetime import timedelta


log = log_config("user service")


class UserService:
    def __init__(self, user_repository: UserRepository = Depends()):
        self.user_repository: UserRepository = user_repository

    # 유저 생성
    def create_user(self, create_user: CreateUser) -> dict:
        """유저 생성
        Return:
            응답데이터 생성
        """

        # 중복 체크
        user = self.user_repository.get_user(create_user.email)
        if not user:
            # password bcrypt
            user_pw = get_cryptcontext(create_user.password)
            self.user_repository.create_user_data(user=User(email=create_user.email, password=user_pw))
        else:
            return {"message": "중복 데이터가 존재합니다.", "status": "duplication"}

        return {"message": "저장을 완료 하였습니다.", "status": "ok"}

    # 이메일, 패스워드 체크
    def check_email_password_user(self, email, password: str) -> bool:
        """이메일, 패스워드 체크
        Args:
            email:
            password:
        Return
            로그인 확인 True, 로그인 실패 False
        """
        check_bool = False
        user: User | None = self.user_repository.get_user(email=email)
        # 유저가 존재 한다면 입력 비번과 디비 정보 비번 비교
        if user:
            check = verify_password(password, user.password)
            if check:
                check_bool = True
        return check_bool

    # 로그인
    def login(self, user: CreateUser) -> dict:
        """로그인을 한다.
        Return:
            dict: access token, token type
        """
        log.debug(" login start ")
        check_password = self.check_email_password_user(user.email, user.password)

        # 유저가 존재 한다면 입력 비번과 디비 정보 비번 비교
        if check_password:
            # token 생성
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="아이디와 비번이 틀렸습니다.")

        return {"access_token": access_token, "token_type": "bearer"}

    # 내정보
    def me(self, email) -> BaseUser:
        """내 정보 데이터
        Return:
            BaseUser: 유저 데이터
        """
        user = self.user_repository.get_user(email)
        return BaseUser(id=user.id, email=user.email)
