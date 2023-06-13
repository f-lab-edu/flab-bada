class SendOk:
    def __init__(self, message: str, content: str):
        self.message = message
        self.content = content

    def __str__(self):
        return f"message: {self.message}, content = {self.content}"
