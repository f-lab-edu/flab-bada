# from flab_bada.schemas.lectures import CreateLecture
# from flab_bada.domain.lecture.lectures_service import LecturesService, LectureRepository
# from flab_bada.database.database import ConnDb
#
#
# def test_create_lecture():
#
#     # user_id 가져와야 한다.
#     user_id = 1
#
#     name = "파이썬 강의"
#     doc = "파이썬 입문자 강의 입니다."
#     user_service = LecturesService(lecture_repository=LectureRepository(ConnDb().get_session()))
#     ret_data = user_service.create_lecture(CreateLecture(
#         user_id=user_id, name=name, doc=doc
#     ))
#
#     assert ret_data != ""
