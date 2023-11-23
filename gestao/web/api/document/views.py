from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from gestao.db.models.user import User
from gestao.web.api.document.utils import generate_affiliation_file

router = APIRouter()


@router.get("/affiliation/{user_id}")
async def get_user_affiliation(user_id: str) -> None:
    user = await User.objects.get(id=user_id)
    file_stream = generate_affiliation_file(user)
    return StreamingResponse(
        file_stream,
        media_type=(
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        ),
    )
