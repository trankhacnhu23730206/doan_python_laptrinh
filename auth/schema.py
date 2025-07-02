from pydantic import BaseModel

class CreateUserAuthRequest(BaseModel):
    email: str
    password: str