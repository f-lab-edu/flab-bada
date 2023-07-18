from pydantic import BaseModel


class CreateLecture(BaseModel):
    user_id: int
    name: str
    doc: str

    class Config:
        schema_extra = {
            "example": {
                "name": "python",
                "doc": "기초 파이썬에 대한 강의이다.",
            }
        }


class ReturnLecture(BaseModel):
    id: int
    user_id: int
    name: str
    doc: str
    # user: dict
