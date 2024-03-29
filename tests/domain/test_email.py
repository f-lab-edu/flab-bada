from flab_bada.domain.email.email_service import EmailService
from flab_bada.domain.email.email_repository import FakeEmailRedisRepository
from fastapi.testclient import TestClient
from flab_bada.schemas.users import BaseEmail
from main import app


client = TestClient(app)


# 시크릿 키 생성
def test_make_secret_key():
    email = "jin3137@gmail.com"
    # 회원가입 후 이메일 발송 한다.
    es = EmailService(email_redis_repository=FakeEmailRedisRepository())
    es.make_secret_num(email=email)
    # 메모리 디비에 sceret key 저장
    # es.set_secret_num(email="jin3137@1thefull.com", key=key)
    assert es.get_secret_num(email=email) != ""


# 이메일 시크릿 키 검증
def test_confirm_email_scret_data():
    es = EmailService(email_redis_repository=FakeEmailRedisRepository())
    # key 값을 받는다. (가정 이메일에서)
    key_value = es.get_secret_num(email="jin3137@gmail.com")

    # 해당 키 값과 레디스 키 값을 비교한다.
    verify_bool = es.verify_secret_num(email="jin3137@gmail.com", secret_key=key_value)

    # 해당 키 값에 대해서 비교 True 이면 user table user use_yn 상태 값을 변경한다.
    assert isinstance(verify_bool, bool)


# 이메일 시크릿 키 페이크 레파지토리 검증
def test_confirm_email_scret_data_with_fakeredisrepository():
    es = EmailService(email_redis_repository=FakeEmailRedisRepository())
    email = "jin3137@gmail.com"
    # key 값을 받는다. (가정 이메일에서)
    key_value = es.get_secret_num(email=email)

    fake_repository = FakeEmailRedisRepository()
    fake_repository.set_email_secret_data(email=email, secret_num=key_value)

    email_secret_key_data = fake_repository.get_email_secret_data(email=email)
    check_data = es.verify_secret_num(email=email, secret_key=email_secret_key_data)

    assert check_data is True


# 이메일 발송 후 시크릿 키 검증
def test_send_email_and_vertify_secret_num():
    es = EmailService(email_redis_repository=FakeEmailRedisRepository())
    email = ["jin3137@gmail.com"]

    # 이메일 확인
    # es.send_email(email=EmailSchema(email=email))

    # 페이크 클래스 이메일 확인
    es.make_secret_num(email=email[0])
    secret_key = es.get_secret_num(email=email[0])

    fake_es_repository = FakeEmailRedisRepository()
    fake_es_repository.set_email_secret_data(email=email[0], secret_num=secret_key)

    fake_secret_key = fake_es_repository.get_email_secret_data(email=email[0])
    assert secret_key == fake_secret_key


# 이메일 발송 엔드포인트 테스트
def test_email_send_endpoint():
    resp = client.post(
        "/email/send",
        json={"email": ["jin3137@gmail.com"]},
    )

    assert resp.status_code == 200


# 토큰 생성 후 엔드포인트에 토큰 데이터 확인
def test_email_confirm_endpoint():
    email = "jin3137@gmail.com"
    es = EmailService(email_redis_repository=FakeEmailRedisRepository())
    es.make_confirm_token(base_email=BaseEmail(email=email))

    token_data = es.get_secret_num(email=email)

    resp = client.get(
        "/email/confirm/v2",
        params={
            "email": "jin3137@gmail.com",
            "token": f"{token_data}",
        },
    )

    assert resp.status_code == 200
