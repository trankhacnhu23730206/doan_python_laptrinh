from typing import Optional
from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class UpdateUserRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    phone: Optional[str]


