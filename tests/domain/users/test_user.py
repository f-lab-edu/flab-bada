from flab_bada.schemas.users import CreateUser
from flab_bada.domain.users.user_service import UserService, UserRepository
from flab_bada.database.database import ConnDb
from flab_bada.utils.bcrypt import verify_token


token = ""


class TestUser:

    def test_login(self):
        email = "jin3137@gmail.com"
        password = "dltjdrnr3137"
        user_service = UserService(user_repository=UserRepository(ConnDb().get_session()))

        token_data = user_service.login(CreateUser(email=email, password=password))
        global token
        token = token_data.get("access_token")

        assert token_data.get("access_token") != ""
        assert token_data.get("token_type") == "bearer"

    def test_me(self):
        email: str = verify_token(token)
        user_service = UserService(user_repository=UserRepository(ConnDb().get_session()))
        base_user = user_service.me(email)

        assert base_user.id != ""
        assert base_user.email != ""

    def test_create(self):
        pass

    def test_get_user(self):
        pass
