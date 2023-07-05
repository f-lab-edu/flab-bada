from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from flab_bada.schemas.users import CreateUser, BaseUser, Token
from flab_bada.domain.users.user_service import UserService
from flab_bada.utils.bcrypt import verify_token
from flab_bada.logging.logging import log_config


log = log_config("user controller")


user_router = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


async def auth(token: str = Depends(oauth2_scheme)) -> str:
    """token 체크
    Args:
        token: 토큰 데이터
    Return:
        토큰 확인 되면 email 데이터
    """
    if not token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Sign in for access")
    decode_token_email = verify_token(token)
    return decode_token_email


@user_router.post("/signup", status_code=status.HTTP_200_OK)
async def sign_new_user(user: CreateUser, user_service: UserService = Depends(UserService)) -> dict:
    """회원가입"""
    try:
        # 회원 가입
        message = user_service.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())

    return message


@user_router.post("/login", response_model=Token, status_code=status.HTTP_200_OK)
async def login(data: CreateUser, us: UserService = Depends(UserService)) -> dict:
    """로그인"""
    try:
        ret_data = us.login(data)
    except Exception as e:
        raise e

    return ret_data


@user_router.get(
    "/users/me",
    response_model=BaseUser,
    status_code=status.HTTP_200_OK,
)
async def me(email: str = Depends(auth), user_service: UserService = Depends(UserService)):
    """내정보"""
    try:
        user_data = user_service.me(email)
    except Exception as e:
        raise e
    return user_data


# role 변경 일반사용자에서 선생님으로 변경한다.
@user_router.put("/users/role/{id}", status_code=status.HTTP_200_OK)
# async def change_role(id: int, Authorization: str = Header("Authorization")):
async def change_role(id: int, email: str = Depends(auth), user_service: UserService = Depends(UserService)):
    """role 변경"""
    try:
        log.info(f"email: {email}")
        user_service.change_role(id, email)
    except Exception as e:
        raise e
    return {"message": "role has been changed"}
