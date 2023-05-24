import pytest

from flab_bada.schemas.users import CreateUser
from flab_bada.domain.users.user_service import UserService
from flab_bada.models.users import User
from flab_bada.schemas.users import BaseUser
from flab_bada.domain import AbstractRepository
from typing import Type


class FakeUserRepository(AbstractRepository):
    def __init__(self):
        self.users = set()

    def create_user_data(self, user: CreateUser) -> CreateUser:
        """사용자 생성
        Args:
            user: 가입 유저 데이터
        Return:
            CreateUser: user
        """
        id_count = len(self.users)
        self.users.add(User(id=id_count, email=user.email, password=user.password, use_yn="Y"))
        return user

    def get_user(self, email: str) -> Type[User] | None:
        for user in self.users:
            user_email = user.email
            if user_email == email:
                return user
        return None


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
        user_service = UserService(user_repository=FakeUserRepository())
        user_service.create_user(CreateUser(email=email, password=password))

        cls.user_service = user_service

    def test_create(self):
        ret_data = self.user_service.create_user(CreateUser(email=self.email, password=self.password))

        assert ret_data != ""
        assert isinstance(ret_data, dict)

    def test_get_user_data(self):
        ret_data = self.user_service.me(email="jin3137@gmail.com")
        assert ret_data != ""
        assert isinstance(ret_data, BaseUser)

    def test_login(self):
        token_data = self.user_service.login(CreateUser(email=self.email, password=self.password))

        assert token_data.get("access_token") != ""
        assert token_data.get("token_type") == "bearer"
