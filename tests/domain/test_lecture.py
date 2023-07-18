from flab_bada.domain.lecture.lectures_repository import FakeLectureRepository
from flab_bada.domain.lecture.lectures_service import LecturesService
from flab_bada.schemas.lectures import CreateLecture


# 강사를 등록한다. FakeRepository를 사용한다.
def test_create_lecture():
    create_lecture = CreateLecture(user_id=1, name="python 강의", doc="python 강의", role="teacher")
    lecture_service = LecturesService(FakeLectureRepository())
    lecture_service.create_lecture(create_lecture=create_lecture)


class TestLecture:
    @classmethod
    def setup_class(cls):
        cls.lecture_service = LecturesService(FakeLectureRepository())

        # 강의를 등록한다.
        create_lecture = CreateLecture(user_id=1, name="python 강의", doc="python 강의", role="teacher")
        # cls.lecture_service.create_lecture(create_lecture=create_lecture)
        cls.lecture_service.create_lecture(create_lecture=create_lecture)

    # 강사를 조회한다.
    def test_get_user(self):
        user_id = 1
        role = "teacher"
        # 강사를 조회한다.
        lecture = self.lecture_service.get_user(user_id=user_id, role=role)
        assert lecture.user_id == 1

    # 등록된 강의를 조회한다. 강의 값이 존재
    def test_get_lecture_data(self):
        """등록된 강의를 조회한다. 강의 값이 존재"""
        lecture_id = 1

        # 강의를 조회한다.
        lecture = self.lecture_service.get_lecture(lecture_id=lecture_id)
        assert lecture.id == 1

    # 강의 값이 존재 하지 않을때
    def test_get_lecture_no_data(self):
        """강의 값이 존재 하지 않는다."""
        lecture_id = 2

        # 강의를 조회한다.
        lecture = self.lecture_service.get_lecture(lecture_id=lecture_id)
        assert lecture.get("message") == "강의가 존재하지 않습니다."

    # 강사의 강의를 조회한다.
    def test_get_lectures_by_teacher(self):
        """강사의 강의를 조회"""
        tearcher_id = 1

        # 강의를 조회한다.
        lectures = self.lecture_service.get_lectures_by_teacher(tearcher_id)

        # 데이터가 존재 하지 않을 때
        if type(lectures) == dict:
            assert lectures.get("message") == "강의가 존재하지 않습니다."
        else:
            # 첫번째 강의 데이터
            assert lectures[0].id == 1
