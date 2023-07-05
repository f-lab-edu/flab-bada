from pydantic import BaseModel


class SendOk(BaseModel):
    message: str
    content: str

    def __str__(self):
        return f"message: {self.message}, content = {self.content}"
