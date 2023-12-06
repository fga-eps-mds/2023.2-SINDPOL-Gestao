from typing import List

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from gestao.db.models.user import User
from gestao.web.api.document.utils import generate_report_users_file

router = APIRouter()


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
