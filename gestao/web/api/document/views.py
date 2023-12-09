import logging
from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from gestao.db.models.user import User
from gestao.web.api.document.utils import (
    generate_affiliation_file,
    generate_report_users_file,
)

router = APIRouter()


@router.get("/affiliation/{user_id}")
async def get_user_affiliation(user_id: str) -> None:
    try:
        user = await User.objects.get(id=user_id)
        file_stream = generate_affiliation_file(user)
        file_name = "affiliation-doc.docx"
        return StreamingResponse(
            file_stream,
            media_type=(
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            ),
            headers={
                "Content-Disposition": f"attachment; filename={file_name}",
            },
        )
    except Exception:
        logging.error("Error occurred while get user", exc_info=True)
        raise HTTPException(status_code=404, detail="User not found")


@router.get("/report-users/")
async def get_report_users(filter_list: List[str] = []):
    users_list = await User.objects.all()
    file_stream = generate_report_users_file(list(users_list), filter_list)
    file_name = "report-users.xlsx"
    return StreamingResponse(
        file_stream,
        media_type=(
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ),
        headers={
            "Content-Disposition": f"attachment; filename={file_name}",
        },
    )
