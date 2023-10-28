import logging
from typing import List
from uuid import uuid4

from fastapi import APIRouter, HTTPException

from gestao.db.models.dependent import Dependent
from gestao.db.models.user import User
from gestao.web.api.dependent.schema import CreateUserDependentDTO, UpdateUserDependentDTO


router = APIRouter()


@router.get("/{user_id}")
async def get_dependents(user_id: str) -> List[Dependent]:
    try:
        user = await User.objects.select_related(User.dependents).get(id=user_id)
        return user.dependents
    except Exception:
        logging.error("Error occurred while get dependents", exc_info=True)
        raise HTTPException(status_code=404, detail="Dependents not found")


@router.post("/{user_id}")
async def create_dependent(user_id: str, create_dependent: CreateUserDependentDTO) -> Dependent:
    try:
        dependent_dict = create_dependent.dict()
        dependent_id = str(uuid4())
        await Dependent.objects.create(id=dependent_id, user_id=user_id, **dependent_dict)
        return await Dependent.objects.get(id=dependent_id)
    except Exception:
        logging.error("Error occurred while creating dependent", exc_info=True)
        raise HTTPException(status_code=400, detail="Error occurred while creating dependent")


@router.put("/{dependent_id}")
async def update_dependent(dependent_id: str, update_dependent: UpdateUserDependentDTO) -> Dependent:
    try:
        await Dependent.objects.filter(id=dependent_id).update(
            each=True,
            **update_dependent.dict(exclude_none=True)
        )
        return await Dependent.objects.get(id=dependent_id)
    except Exception:
        logging.error("Error occurred while updating dependent", exc_info=True)
        raise HTTPException(status_code=404, detail="Error occurred while updating dependent")


@router.delete("/{dependent_id}")
async def delete_dependent(dependent_id: str) -> None:
    try:
        await Dependent.objects.delete(id=dependent_id)
    except Exception:
        logging.error("Error occurred while deleting dependent", exc_info=True)
        raise HTTPException(status_code=404, detail="Error occurred while deleting dependent")


