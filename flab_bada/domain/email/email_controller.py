from fastapi import APIRouter, status, Depends, HTTPException
from starlette.responses import JSONResponse
from flab_bada.schemas.users import EmailSecret
from flab_bada.domain.email.email_service import EmailService
from flab_bada.logging.logging import log_config
from flab_bada.schemas.users import EmailSchema
from flab_bada.response.ok_response import SendOk


log = log_config("email controller")


email_router = APIRouter()


@email_router.post("/email/send")
async def simple_send(email_schema: EmailSchema, email_service: EmailService = Depends()) -> JSONResponse:
    try:
        email_service.send_email(email_schema)
    except Exception as e:
        log.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.__str__())
    return SendOk(message="email has been sent", content="ok")


@email_router.post("/email/confirm", status_code=status.HTTP_200_OK)
async def confirm_email(email_secret: EmailSecret, email_service: EmailService = Depends()) -> JSONResponse:
    try:
        check_data = email_service.verify_secret_num(email=email_secret.email, secret_key=email_secret.secret_num)
        # False 인증 불일치
        if not check_data:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="인증번호를 잘못입력하였습니다.")
    except Exception as e:
        raise e
    return SendOk(message="인증되었습니다.", content="ok")
