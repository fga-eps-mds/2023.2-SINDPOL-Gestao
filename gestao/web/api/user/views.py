import logging
from typing import List
from uuid import uuid4

from fastapi import APIRouter, HTTPException

from gestao.db.models.dependent import Dependent
from gestao.db.models.user import User
from gestao.web.api.user.schema import CreateUserDTO, UpdateUserDTO, AuthUserDTO

router = APIRouter()


@router.get("/", response_model_exclude={"dependents__user_id"})
async def get_users(
    limit: int = 10,
    offset: int = 0,
) -> List[User]:
    return await User.objects.limit(limit).offset(offset).all()


@router.get("/{user_id}", response_model_exclude={"dependents__user_id"})
async def get_user(user_id: str) -> User:
    try:
        return await User.objects.select_related(User.dependents).get(id=user_id)
    except Exception:
        logging.error("Error occurred while get user", exc_info=True)
        raise HTTPException(status_code=404, detail="User not found")


@router.post("/", response_model_exclude={"dependents__user_id"})
async def create_user(create_user: CreateUserDTO) -> User:
    try:
        create_user_dict = create_user.dict()
        dependents = create_user_dict.pop("dependents", [])
        user_id = str(uuid4())
        await User.objects.create(id=user_id, **create_user_dict)
        if dependents:
            await Dependent.objects.bulk_create(
                [
                    Dependent(id=str(uuid4()), user_id=user_id, **dependent)
                    for dependent in dependents
                ],
            )
        return await User.objects.select_related(User.dependents).get(id=user_id)
    except Exception:
        logging.error("Error occurred while creating user", exc_info=True)
        raise HTTPException(
            status_code=400,
            detail="Error occurred while creating user",
        )


@router.put("/{user_id}", response_model_exclude={"dependents__user_id"})
async def update_user(user_id: str, update_user: UpdateUserDTO) -> User:
    try:
        await User.objects.filter(id=user_id).update(
            each=True,
            **update_user.dict(exclude_none=True),
        )
        return await User.objects.select_related(User.dependents).get(id=user_id)
    except Exception:
        logging.error("Error occurred while updating user", exc_info=True)
        raise HTTPException(
            status_code=404,
            detail="Error occurred while updating user",
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


@router.get("_auth/login")
async def user_auth(user_data: AuthUserDTO) -> User:
    try:
        user_data_dict = user_data.dict()
        return await User.objects.get(
            registration=user_data_dict['registration'],
            password=user_data_dict['password']
        )
    except Exception:
        logging.error("Error occurred in user_login", exc_info=True)
        raise HTTPException(status_code=404, detail="Error occurred in login user")


