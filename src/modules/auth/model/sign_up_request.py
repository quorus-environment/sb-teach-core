from pydantic import BaseModel


class SignUpRequest(BaseModel):
    username: str
    email: str
    password: str
    role: str

    first_name: str
    last_name: str
    second_name: str
