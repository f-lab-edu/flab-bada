from flab_bada.database.database import SessionLocal
from flab_bada.models.users import User
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from main import app
from flab_bada.utils.bcrypt import verify_token


client = TestClient(app)


class TestUsers:

    def test_insert_users(self, db: Session = SessionLocal):
        """
            회원가입
            id = Column(Integer, primary_key=True, index=True)
            email = Column(String, unique=True, index=True)
            password = Column(String)
            is_active = Column(String, default='Y')
        Args:
            db: 데이터 베이스 연동
        """

        user = User(
            email="jin3137@gmail.com",
            password="dltjdrnr3137",
            is_active="Y",
        )
        with db.begin() as session:
            session.add(user)
            session.commit()
            session.flush(user)
        print(user)

    def test_login(self):
        resp = client.post(
            "/login",
            json={"email": "jin3137@gmail.com", "password": "dltjdrnr3137"},
        )

        print(f"\n\t response: {resp.text}")
        assert resp.status_code == 200

    # def test_me(self):
    #     token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqaW4zMTM3QGdtYWlsLmNvbSIsImV4cCI6MTY4MjY2NDg1MX0.IPRG09N8fFCGXvHykbPoGQ6MCvAC1pjnu8_H4PWpQjE"
    #     resp = client.get(
    #         "/users/me",
    #         headers={"Authorization": f"Bearer {token}"}
    #     )
    #
    #     print(f"\n\t response: {resp.text}")
    #     assert resp.status_code == 200
