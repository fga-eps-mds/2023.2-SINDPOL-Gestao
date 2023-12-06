import logging

from fastapi import APIRouter, HTTPException, Request

from gestao.db.models.user import User
from gestao.web.api.login.schemas import AuthUserDTO, RecoverPasswordDTO
from gestao.web.api.login.utils import generate_password, send_email

router = APIRouter()


@router.post("/user")
async def login_user(login_data: AuthUserDTO) -> User:
    try:
        return await User.objects.select_related(User.dependents).get(
            **login_data.dict()
        )
    except Exception:
        logging.error("User not found", exc_info=True)
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )


@router.post("/recover-password")
async def recover_password(request: Request, recover_data: RecoverPasswordDTO) -> None:
    try:
        url_logo = str(request.url_for("static", path="logo.png"))
        user = await User.objects.get(**recover_data.dict())
        new_password = generate_password()
        send_email(
            user_name=user.fullName,
            user_email=user.email,
            new_password=new_password,
            logo_path=url_logo,
        )
        await user.update(password=new_password)
    except Exception:
        logging.error("Error occurred while sending email", exc_info=True)
        raise HTTPException(
            status_code=400, detail="Error occurred while sending email"
        )
