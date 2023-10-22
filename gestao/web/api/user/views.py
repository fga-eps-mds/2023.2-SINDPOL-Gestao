from typing import List
from uuid import uuid4

from fastapi import APIRouter, HTTPException

from gestao.db.models.user import User
from gestao.web.api.user.schema import CreateUserDTO, UpdateUserDTO

router = APIRouter()


@router.get("/")
async def get_users(
    limit: int = 10,
    offset: int = 0,
) -> List[User]:
    return await User.objects.limit(limit).offset(offset).all()


@router.get("/{user_id}")
async def get_user(user_id: str) -> User:
    try:
        return await User.objects.get(id=user_id)
    except Exception:
        raise HTTPException(status_code=404, detail="User not found")


@router.post("/")
async def create_user(create_user: CreateUserDTO) -> User:
    try:
        return await User.objects.create(
            **{
                "id": str(uuid4()),
                **create_user.dict(),
            }
        )
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Error occurred while creating user",
        )


@router.put("/{user_id}")
async def update_user(user_id: str, update_user: UpdateUserDTO) -> User:
    try:
        await User.objects.filter(id=user_id).update(
            each=True,
            **update_user.dict(exclude_none=True),
        )
        return await User.objects.get(id=user_id)
    except Exception:
        raise HTTPException(
            status_code=404,
            detail="Error occurred while updating user",
        )


@router.delete("/{user_id}")
async def delete_user(user_id: str) -> None:
    try:
        await User.objects.delete(id=user_id)
    except Exception:
        raise HTTPException(
            status_code=404,
            detail="Error occurred while deleting user",
        )
