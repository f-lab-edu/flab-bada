from flab_bada.domain.email.email_service import EmailService
from flab_bada.domain import AbstractRepository


class FakeEmailRedisRepository(AbstractRepository):
    def __init__(self):
        self.email_secret_data = dict()

    def set_email_secret_data(self, email: str, secret_num: str) -> None:
        self.email_secret_data[email] = secret_num

    def get_email_secret_data(self, email) -> str:
        return self.email_secret_data.get(email)


def test_make_secret_key():
    # 회원가입 후 이메일 발송 한다.
    es = EmailService()

    # 메모리 디비에 sceret key 저장
    es.set_secret_num(email="jin3137@gmail.com")


def test_confirm_email_scret_data():
    es = EmailService()
    # key 값을 받는다. (가정 이메일에서)
    key_value = es.get_secret_num(email="jin3137@gmail.com")

    # 해당 키 값과 레디스 키 값을 비교한다.
    verify_bool = es.verify_secret_num(email="jin3137@gmail.com", secret_key=key_value)

    # 해당 키 값에 대해서 비교 True 이면 user table user use_yn 상태 값을 변경한다.
    assert isinstance(verify_bool, bool)


def test_confirm_email_scret_data_with_fakeredisrepository():
    es = EmailService()
    email = "jin3137@gmail.com"
    # key 값을 받는다. (가정 이메일에서)
    key_value = es.get_secret_num(email=email)

    fake_repository = FakeEmailRedisRepository()
    fake_repository.set_email_secret_data(email=email, secret_num=key_value)

    email_secret_key_data = fake_repository.get_email_secret_data(email=email)

    check_data = es.verify_secret_num(email=email, secret_key=email_secret_key_data)

    assert check_data is True
