from datetime import timedelta
from flab_bada.utils.bcrypt import create_access_token


class TestBcrypt:

    def test_create_token(self):
        email = "jin3137@gmail.com"
        access_token_expires = timedelta(seconds=60)
        access_token = create_access_token(
            data={"sub": email}, expires_delta=access_token_expires
        )
        assert access_token != ""
