from fastapi import Depends, APIRouter, HTTPException, status
from flab_bada.domain.lecture.lectures_service import LecturesService
from flab_bada.logging.logging import log_config
from flab_bada.schemas.lectures import ReturnLecture


log = log_config("lecture controller")


lecture_router = APIRouter()


# 강의 조회
@lecture_router.get("/lectures/{lecture_id}", status_code=status.HTTP_200_OK)
async def get_lecture(lecture_id: int, lecture_service: LecturesService = Depends()) -> ReturnLecture | dict:
    try:
        # 강의 조회
        lecture = lecture_service.get_lecture(lecture_id=lecture_id)
    except Exception as e:
        log.error(e)
        raise HTTPException(status_code=500, detail=e.__str__())

    return lecture
