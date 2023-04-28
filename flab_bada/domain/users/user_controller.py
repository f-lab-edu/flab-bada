from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from flab_bada.schemas.users import CreateUser, BaseUser, Token
from flab_bada.utils.bcrypt import get_cryptcontext
from flab_bada.domain.users.user_service import UserService
from sqlalchemy.orm import Session
from flab_bada.database.database import get_db
from flab_bada.utils.bcrypt import verify_token


user_router = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/me")


async def auth(token: str = Depends(oauth2_scheme)) -> str:
    """token 체크
    Args:
        token: 토큰 데이터
    Return:
        토큰 확인 되면 email 데이터
    """
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Sign in for access"
        )
    decode_token_email = verify_token(token)
    return decode_token_email


@user_router.post("/signup", status_code=status.HTTP_200_OK)
async def sign_new_user(data: CreateUser, db: Session = Depends(get_db)) -> dict:
    """회원가입"""
    try:
        # todo: email checking, email 중복 checking
        user_email = data.email
        # password bcrypt
        user_pw = get_cryptcontext(data.password)

        us = UserService(email=user_email, pw=user_pw)

        # 회원 가입
        message = us.create_user(db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())

    return message


@user_router.post("/login", response_model=Token, status_code=status.HTTP_200_OK)
async def login(data: CreateUser, db: Session = Depends(get_db)) -> dict:
    """로그인"""
    try:
        email = data.email
        pw = data.password

        us = UserService(email=email, pw=pw)
        ret_data = us.login(db)
    except Exception as e:
        raise e

    return ret_data


@user_router.get("/users/me", response_model=BaseUser, status_code=status.HTTP_200_OK)
async def me(db: Session = Depends(get_db), email: str = Depends(auth)):
    """내정보"""
    try:
        print(f"email: {email}")
        us = UserService(email=email)
        user = us.me(db)
    except Exception as e:
        raise e
    return user
