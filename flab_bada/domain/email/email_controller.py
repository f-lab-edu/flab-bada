from fastapi import APIRouter, status, Depends, HTTPException
from pydantic import EmailStr, BaseModel
from typing import List
from starlette.responses import JSONResponse
from flab_bada.schemas.users import EmailSecret
from flab_bada.domain.email.email_service import EmailService
from flab_bada.logging.logging import log_config


log = log_config("email controller")


email_router = APIRouter()


class EmailSchema(BaseModel):
    email: List[EmailStr]


@email_router.post("/send/email")
async def simple_send(email: EmailSchema, email_service: EmailService = Depends()) -> JSONResponse:
    try:
        email_service.send_email(email)
    except Exception as e:
        log.error(e)
        return JSONResponse(status_code=500, content={"message": e.__str__()})
    return JSONResponse(status_code=200, content={"message": "email has been sent"})


@email_router.post("/confirm/email", status_code=status.HTTP_200_OK)
async def confirm_email(email: EmailSecret, email_service: EmailService = Depends()) -> JSONResponse:
    try:
        check_data = email_service.verify_secret_num(email=email.email, secret_key=email.secret_num)
        # False 인증 불일치
        if not check_data:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="인증번호를 잘못입력하였습니다.")
    except Exception as e:
        raise e

    return JSONResponse(status_code=200, content={"message": "인증되었습니다."})
