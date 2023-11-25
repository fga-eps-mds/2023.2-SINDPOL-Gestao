from pydantic import BaseModel


class AuthUserDTO(BaseModel):
    registration: str
    password: str
