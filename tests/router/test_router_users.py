# from flab_bada.database.database import SessionLocal
# from sqlalchemy.orm import Session
# from fastapi.testclient import TestClient
# from main import app
#
#
# token = ""
# client = TestClient(app)
#
#
# class TestUsers:
#     def test_insert_users(self, db: Session = SessionLocal):
#         """
#             회원가입
#             id = Column(Integer, primary_key=True, index=True)
#             email = Column(String, unique=True, index=True)
#             password = Column(String)
#             is_active = Column(String, default='Y')
#         Args:
#             db: 데이터 베이스 연동
#         """
#         resp = client.post(
#             "/signup",
#             json={"email": "jin3137@gmail.com", "password": "dltjdrnR#!37"},
#         )
#         assert resp.status_code == 200
#
#     def test_login(self):
#         resp = client.post(
#             "/login",
#             json={"email": "jin3137@gmail.com", "password": "dltjdrnR#!37"},
#         )
#         assert resp.status_code == 200
#         global token
#         token = resp.json().get("access_token")
#
#     def test_me(self):
#         resp = client.get("/users/me", headers={"Authorization": f"Bearer {token}"})
#         assert resp.status_code == 200

# 일반 사용자에서 선생님으로 변경
# def test_endpoint_update_user_status_data(self):
#     # 토큰 값을 받아온다.
#     token_data = self.user_service.login(CreateUser(email=self.email, password=self.password))
#
#     assert token_data.get("access_token") != ""
#
#     client.put(
#         "/users/role/1",
#         headers={
#             "Authorization": f"{token_data.get('token_type')} {token_data.get('access_token')}",
#         },
#     )
