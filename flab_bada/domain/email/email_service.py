import secrets
from fastapi_mail import ConnectionConfig
from pydantic import EmailStr, BaseModel
from typing import List
from flab_bada.database.database import RedisConn
from flab_bada.logging.logging import log_config


log = log_config("email service")


class EmailSchema(BaseModel):
    email: List[EmailStr]


# 이메일 세팅 값 아직 개발중 개발완료 되면 env 환경 세팅 부분으로 이동
conf = ConnectionConfig(
    MAIL_USERNAME="jin3137",
    MAIL_PASSWORD="luzrpslqymtuxjkj",
    MAIL_FROM="jin3137@gmail.com",
    MAIL_PORT=587,
    # MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="Gmail",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=False,
    VALIDATE_CERTS=False,
)


class EmailService:
    def __init__(self):
        self.key_num = 16
        self.redis = RedisConn().get_session()
        # self.redis_repository = redis_repository

    def send_email(self, email: EmailSchema):
        pass

    def make_secret_num(self) -> str:
        """파이썬 시크릿 클래스에 제공하는 토큰 값"""
        key = secrets.token_hex(self.key_num)
        return key

    def set_secret_num(self, email: str) -> None:
        """인증번호를 저장한다.
        Args:
            email: 이메일 주소
        """
        key = self.make_secret_num()
        log.info(f" key vale : {key}")
        # 이메일, key 값을 레디스에 저장한다.
        self.redis.set(email, key)

    def get_secret_num(self, email: str) -> str:
        return self.redis.get(email)

    def verify_secret_num(self, email: str, secret_key: str) -> bool:
        """인증번호 검사
        Args:
            email: 이메일 주소
            secret_key: 받은 데이터 값
        Return:
            check_data: bool -> 비교 검사 데이터
        """
        check_data = False

        # 메모리디비에서 값을 얻는다.
        mem_secret_key = self.get_secret_num(email)
        if secret_key == mem_secret_key:
            check_data = True
        return check_data
