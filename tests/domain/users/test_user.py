from flab_bada.schemas.users import CreateUser
from flab_bada.domain.users.user_service import UserService, UserRepository
from flab_bada.database.database import ConnDb
from flab_bada.utils.bcrypt import verify_token


class TestUser:

    def test_create(self):
        email = "jin3137@gmail.com"
        password = "dltjdrnr3137"
        user_service = UserService(user_repository=UserRepository(ConnDb().get_session()))
        ret_data = user_service.create_user(CreateUser(email=email, password=password))

        assert ret_data != ""

    def test_login_and_me(self):
        email = "jin3137@gmail.com"
        password = "dltjdrnr3137"
        user_service = UserService(user_repository=UserRepository(ConnDb().get_session()))
        token_data: dict = user_service.login(CreateUser(email=email, password=password))
        # token = token_data.get("access_token")
        assert token_data.get("access_token") != ""
        assert token_data.get("token_type") == "bearer"

        # email: str = verify_token(token)
        # base_user = user_service.me(email)

        # assert base_user.id != ""
        # assert base_user.email != ""
