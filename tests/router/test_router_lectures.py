# from fastapi.testclient import TestClient
# from main import app


# client = TestClient(app)


# # endpoint test 등록된 강의를 조회한다. 강의 값이 존재
# def test_get_lecture_data():
#     lectures = client.get("/lectures/1")
#     assert lectures.status_code == 200
#     assert lectures.json().get("id") == 1


# # endpoint test 등록된 강의가 조회한다. 강의 값이 존재 하지 않을때
# def test_get_lecture_no_data():
#     lectures = client.get("/lectures/4")
#     assert lectures.status_code == 200
#     assert lectures.json().get("message") == "강의가 존재하지 않습니다."


# endpoint test 강사의 강의를 조회한다.
# def test_get_lectures_by_tearcher():
#     pass
