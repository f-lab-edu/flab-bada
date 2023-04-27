from dataclasses import dataclass
from pydantic import BaseModel


class BaseUser(BaseModel):
    id: int
    email: str


class CreateUser(BaseModel):
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "jin3137@gmail.com",
                "password": "qweasd#!",
            }
        }


class Token(BaseModel):
    access_token: str
    token_type: str
