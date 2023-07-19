import pytest

from flab_bada.domain.users.user_repository import FakeUserRepository
from flab_bada.domain.email.email_service import EmailService
from flab_bada.domain.email.email_repository import FakeEmailRedisRepository
from flab_bada.schemas.users import CreateUser
from flab_bada.domain.users.user_service import UserService
from flab_bada.schemas.users import BaseUser
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


class TestUserSignup:
    @classmethod
    def setup_class(cls):
        email = "jin3137@gmail.com"
        password = "dltjdrnR#!37"
        cls.email = email
        cls.password = password
        # user_service = UserService(user_repository=FakeUserRepository())

    def test_validator_email(self):
        CreateUser(email=self.email, password=self.password)

    def test_validator_password(self):
        email = "jin3137@gmail.com"
        password = "dltjdrnr3137"

        with pytest.raises(ValueError):
            CreateUser(email=email, password=password)

    def test_validator_your_email(self):
        pass


class TestUser:
    @classmethod
    def setup_class(cls):
        email = "jin3137@gmail.com"
        password = "dltjdrnR#!37"
        cls.email = email
        cls.password = password
        user_service = UserService(
            user_repository=FakeUserRepository(), email_service=EmailService(FakeEmailRedisRepository())
        )
        user_service.create_user(CreateUser(email=email, password=password))

        cls.user_service = user_service

    # 유저 생성
    def test_create(self):
        ret_data = self.user_service.create_user(CreateUser(email=self.email, password=self.password))

        assert ret_data != ""
        assert isinstance(ret_data, dict)

    # 유저 정보 조회
    def test_get_user_data(self):
        ret_data = self.user_service.me(email="jin3137@gmail.com")
        assert ret_data != ""
        assert isinstance(ret_data, BaseUser)

    # 로그인 테스트
    def test_login(self):
        token_data = self.user_service.login(CreateUser(email=self.email, password=self.password))

        assert token_data.get("access_token") != ""
        assert token_data.get("token_type") == "bearer"


class TestUserDetail:
    @classmethod
    def setup_class(cls):
        """임시 유저 생성"""
        email = "jin3137@outlook.com"
        password = "dltjdrnR#!37"
        cls.email = email
        cls.password = password
        user_service = UserService(user_repository=FakeUserRepository())
        user_service.create_user(CreateUser(email=email, password=password))

        cls.user_service = user_service
