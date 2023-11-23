from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from gestao.db.models.user import User
from gestao.web.api.document.utils import generate_affiliation_file, convert_file

router = APIRouter()


@router.get("/affiliation/{user_id}")
async def get_user_affiliation(user_id: str) -> None:
    try:
        user = await User.objects.get(id=user_id)
        file_stream = generate_affiliation_file(user)
        pdf_file_stream = convert_file(file_stream)
        return StreamingResponse(
            pdf_file_stream,
            media_type=(
                "application/pdf"
            ),
        )
    except Exception:
        logging.error("Error occurred while get user", exc_info=True)
        raise HTTPException(status_code=404, detail="User not found")
