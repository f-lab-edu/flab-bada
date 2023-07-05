from flab_bada.domain.lecture.lectures_repository import FakeLectureRepository
from flab_bada.domain.lecture.lectures_service import LecturesService
from flab_bada.schemas.lectures import CreateLecture


# 강사를 등록한다. FakeRepository를 사용한다.
def test_create_lecture():
    create_lecture = CreateLecture(user_id=1, name="python 강의", doc="python 강의")
    lecture_service = LecturesService(FakeLectureRepository())
    lecture_service.create_lecture(create_lecture=create_lecture)


class TestLecture:
    @classmethod
    def setup_class(cls):
        cls.lecture_service = LecturesService(FakeLectureRepository())

        # 강의를 등록한다.
        create_lecture = CreateLecture(user_id=1, name="python 강의", doc="python 강의")
        cls.lecture_service.create_lecture(create_lecture=create_lecture)

    def test_get_user(self):
        # 강사를 조회한다.
        lecture = self.lecture_service.get_user(user_id=1)
        assert lecture.user_id == 1

    def test_get_lecture(self):
        pass
