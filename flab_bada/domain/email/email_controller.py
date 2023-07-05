from fastapi import APIRouter, status, Depends, HTTPException
from flab_bada.schemas.users import EmailSecret
from flab_bada.domain.email.email_service import EmailService
from flab_bada.logging.logging import log_config
from flab_bada.schemas.users import EmailSchema
from flab_bada.schemas.response_schemas import SendOk
from fastapi.security import OAuth2PasswordBearer
from flab_bada.utils.bcrypt import verify_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


log = log_config("email controller")


email_router = APIRouter()


async def auth(token: str = Depends(oauth2_scheme)) -> str:
    """token 체크
    Args:
        token: 토큰 데이터
    Return:
        토큰 확인 되면 email 데이터
    """
    if not token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="This is not useful information.")
    decode_token_email = verify_token(token)
    return decode_token_email


@email_router.post("/email/send", response_model=SendOk)
async def simple_send(email_schema: EmailSchema, email_service: EmailService = Depends()) -> SendOk:
    try:
        email_service.send_email(email_schema)
    except Exception as e:
        log.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.__str__())
    return SendOk(message="email has been sent", content="ok")


@email_router.get("/email/confirm/v2", response_model=SendOk, status_code=status.HTTP_200_OK)
async def get_confirm_email(token: str) -> SendOk:
    try:
        # check_data = email_service.verify_confirm_token(token=token, email=email)
        verify_token(token=token)

        # 이메일 인증 완료 되었다는 유저 정보 업데이트 추가
    except Exception as e:
        log.error(e)
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="유요한 정보가 아닙니다.")
    return SendOk(message="인증되었습니다.", content="ok")


@email_router.post("/email/confirm", response_model=SendOk, status_code=status.HTTP_200_OK)
async def confirm_email(email_secret: EmailSecret, email_service: EmailService = Depends()) -> SendOk:
    try:
        check_data = email_service.verify_secret_num(email=email_secret.email, secret_key=email_secret.secret_num)
        # False 인증 불일치
        if not check_data:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="인증번호를 잘못입력하였습니다.")
    except Exception as e:
        raise e
    return SendOk(message="인증되었습니다.", content="ok")
