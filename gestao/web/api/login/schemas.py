from pydantic import BaseModel


class AuthUserDTO(BaseModel):
    registration: str
    password: str


class RecoverPasswordDTO(BaseModel):
    email: str
