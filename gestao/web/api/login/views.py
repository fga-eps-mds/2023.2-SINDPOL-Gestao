import logging

from fastapi import APIRouter, HTTPException

from gestao.db.models.user import User
from gestao.web.api.login.schemas import AuthUserDTO

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
