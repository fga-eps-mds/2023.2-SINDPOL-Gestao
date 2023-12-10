import logging
from typing import List
from uuid import uuid4

from asyncpg.exceptions import UniqueViolationError
from fastapi import APIRouter, HTTPException, Request

from gestao.db.models.dependent import Dependent
from gestao.db.models.user import User
from gestao.web.api.login.utils import generate_password, send_email
from gestao.web.api.user.enums import UserStatus
from gestao.web.api.user.schemas import CreateUserDTO, UpdateUserDTO

router = APIRouter()


@router.get("/", response_model_exclude={"dependents__user_id"})
async def get_users(
    limit: int = 10,
    offset: int = 0,
) -> List[User]:
    return (
        await User.objects.limit(limit)
        .offset(
            offset,
        )
        .all()
    )


@router.get("/{user_id}", response_model_exclude={"dependents__user_id"})
async def get_user(user_id: str) -> User:
    try:
        return await User.objects.select_related(
            User.dependents,
        ).get(id=user_id)
    except Exception:
        logging.error("Error occurred while get user", exc_info=True)
        raise HTTPException(status_code=404, detail="User not found")


@router.post("/", response_model_exclude={"dependents__user_id"})
async def create_user(request: Request, create_user: CreateUserDTO) -> User:
    try:
        create_user_dict = create_user.dict()
        dependents = create_user_dict.pop("dependents", [])
        user_id = str(uuid4())
        user_password = generate_password()
        create_user_dict["password"] = user_password
        url_logo = str(request.url_for("static", path="logo.png"))
        send_email(
            create_user_dict["fullName"],
            create_user_dict["email"],
            user_password,
            url_logo,
        )
        await User.objects.create(
            id=user_id, **create_user_dict, status=UserStatus.analyzing
        )
        if dependents:
            await Dependent.objects.bulk_create(
                [
                    Dependent(id=str(uuid4()), user_id=user_id, **dependent)
                    for dependent in dependents
                ],
            )
        return await User.objects.select_related(User.dependents).get(id=user_id)
    except UniqueViolationError:
        logging.error("User already exists", exc_info=True)
        raise HTTPException(
            status_code=400,
            detail="User already exists",
        )
    except Exception:
        logging.error("Error occurred while creating user", exc_info=True)
        raise HTTPException(
            status_code=400,
            detail="Error occurred while creating user",
        )


@router.put("/{user_id}", response_model_exclude={"dependents__user_id"})
async def update_user(user_id: str, update_user: UpdateUserDTO) -> User:
    try:
        user = await User.objects.get(id=user_id)
        await user.update(**update_user.dict(exclude_none=True))
        return await User.objects.select_related(User.dependents).get(id=user_id)
    except Exception:
        logging.error("User not found", exc_info=True)
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )


@router.delete("/{user_id}")
async def delete_user(user_id: str) -> None:
    try:
        await User.objects.delete(id=user_id)
    except Exception:
        logging.error("Error occurred while deleting user", exc_info=True)
        raise HTTPException(
            status_code=404,
            detail="Error occurred while deleting user",
        )


@router.patch("/{user_id}/disable")
async def disable_user(user_id: str) -> None:
    try:
        user = await User.objects.get(id=user_id)
        await user.update(status=UserStatus.inactive)
        return {"detail": "User disabled successfully"}
    except Exception:
        logging.error("User not found", exc_info=True)
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )


@router.patch("/{user_id}/enable")
async def enable_user(user_id: str) -> None:
    try:
        user = await User.objects.get(id=user_id)
        await user.update(status=UserStatus.active)
        return {"detail": "User enable successfully"}
    except Exception:
        logging.error("User not found", exc_info=True)
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )
