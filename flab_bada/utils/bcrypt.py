from fastapi import HTTPException, status
from flab_bada.logging.logging import log_config
from flab_bada.config.config import token_setting
from passlib.context import CryptContext
from datetime import timedelta, datetime
from jose import jwt, JWTError


log = log_config("utils bcrypt")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = token_setting.SECRET_KEY
REFRESH_SECRET_KEY = token_setting.REFRESH_SECRET_KEY
ALGORITHM = token_setting.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = token_setting.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_MINUTES = token_setting.REFRESH_TOKEN_EXPIRE_MINUTES
CONFIRM_TOKEN_EXPIRE_MINUTES = token_setting.CONFIRM_TOKEN_EXPIRE_MINUTES


def get_cryptcontext(input_data: str) -> str:
    """

    Args:
        input_data: 사용자 비번 데이터
    Return:
        암호된 데이터 리턴
    """
    ret_data = pwd_context.hash(input_data)
    return ret_data


def verify_password(plain_password, hashed_password):
    """

    Args:
        plain_password:
        hashed_password:
    Return:

    """
    return pwd_context.verify(plain_password, hashed_password)


# token 생성
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
        토큰 생성
    Args:
         data:
         expires_delta:
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def refresh_access_token(data: dict, expires_delta: timedelta | None = None):
    """
        토큰 생성
    Args:
         data:
         expires_delta:
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, REFRESH_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_confirm_token(data: dict, expires_delta: timedelta | None = None):
    """
        토큰 생성
    Args:
         data:
         expires_delta:
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    """
        토큰 검사
    Args:
         token: 토큰 데이터
    Return:
        jwt 디코딩된 data
    """
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = data.get("sub")

        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"Authenticate": "Bearer"},
            )
        return email
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token"
        )


def get_email_by_token(token: str) -> str:
    """토큰  활용 이메일 얻기"""
    email = verify_token(token)
    return email
