import secrets
import yagmail

# from flab_bada.database.database import RedisConn
from flab_bada.domain.email.email_repository import EmailRedisRepository
from flab_bada.logging.logging import log_config
from flab_bada.schemas.users import EmailSchema
from fastapi import Depends

log = log_config("email service")


class EmailService:
    def __init__(self, email_redis_repository: EmailRedisRepository = Depends()):
        self.key_num = 16
        # self.redis = RedisConn().get_session()
        # self.email_redis_repository = EmailRedisRepository()
        self.email_redis_repository = email_redis_repository

    def send_email(self, email_schema: EmailSchema) -> None:
        """이메일 인증 보내기
        Args:
            email_schema: 이메일 정보, 시크릿 번호

        Return:
            생성된 secret key 데이터
        """
        try:
            email = email_schema.email[0]
            self.make_secret_num(email=email)
            html = f"""<p>회원 가입을 축하드립니다. 인증키 번호 입니다. {self.get_secret_num(email=email)} 인증 버튼에 복사해 주세요."""
            yag = yagmail.SMTP({"jin3137@gmail.com": "flab-bada"}, "mtveqsvobkhqzlrt")
            yag.send(email_schema.email, "flab bada 회원 인증 메일", html)
        except Exception as e:
            raise e

    def make_secret_num(self, email: str) -> None:
        """파이썬 시크릿 클래스에 제공하는 토큰 값"""
        key = secrets.token_hex(self.key_num)
        self.set_secret_num(email=email, key=key)

    def set_secret_num(self, email: str, key: str) -> None:
        """인증번호를 저장한다.
        Args:
            email: 이메일 주소
            key:
        """
        log.info(f" key vale : {key}")
        # 이메일, key 값을 레디스에 저장한다.
        self.email_redis_repository.set_email_secret_data(email=email, secret_num=key)

    def get_secret_num(self, email: str) -> str:
        return self.email_redis_repository.get_email_secret_data(email=email)

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
