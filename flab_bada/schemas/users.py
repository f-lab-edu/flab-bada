import re

from pydantic import BaseModel, EmailStr, constr, validator
from typing import List


class BaseUser(BaseModel):
    id: int
    email: str


class BaseEmail(BaseModel):
    email: EmailStr


class CreateUser(BaseModel):
    email: EmailStr
    password: constr(max_length=20, strip_whitespace=True)  # 최대 길이

    @validator("password")
    def check_validator(cls, value):
        if not re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#!%*?&])[A-Za-z\d@$#!%*?&]+$", value):
            raise ValueError(" 적어도 대문자, 특수문자, 숫자로 이루어 져야 합니다.")
        return value

    class Config:
        schema_extra = {
            "example": {
                "email": "jin3137@gmail.com",
                "password": "qweasd#!",
            }
        }


class Token(BaseModel):
    access_token: str
    token_type: str | None = None


class EmailSecret(BaseModel):
    email: EmailStr
    secret_num: str


class EmailSchema(BaseModel):
    email: List[EmailStr]


# # 일반 사용자
# class User(BaseUser):
#     name: str = ""
#     received_email: BaseEmail
#     password: str = "" | None
#     use_yn: str = "Y"
#     role: str = "user"


# class Teacher(User):
#     role: str = "teacher"


class Ok(BaseModel):
    message: str
    status: str
