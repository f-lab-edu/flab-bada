from fastapi import APIRouter, status, Depends, HTTPException
from flab_bada.schemas.lectures import CreateLecture
from flab_bada.domain.lecture.lectures_service import LecturesService


lectures = APIRouter(prefix="/v1/lectures")


@lectures.post("/create", status_code=status.HTTP_200_OK)
async def create_lecture(
    lecture: CreateLecture, lecture_service: LecturesService = Depends(LecturesService)
):
    """강의 생성"""
    try:
        lecture_data: CreateLecture = lecture_service.create_lecture(lecture)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())

    return lecture_data
