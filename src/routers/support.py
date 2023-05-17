import fastapi
import config

from src.models.support_request import SupportRequest
from src.services.support import support_service
from typing import Optional

router = fastapi.APIRouter()

@router.post("/user/{user_id}/message")
async def create_message(user_id: int, support_request: SupportRequest):
    try:
        support_service.create_message(user_id, support_request.message)
        return {"status": "Done"}
    except Exception as e:
        return {"status": "Error", "message": str(e)}

@router.post("/support/{support_id}/message")
async def set_support(support_id: int, support_request: SupportRequest):
    try:
        support_service.set_message_support(support_request.message_id, support_id)
        return {"status": "Done"}
    except Exception as e:
        return {"status": "Error", "message": str(e)}

@router.post("/message/answer")
async def respond_message(support_request: SupportRequest):
    try:
        support_service.set_message_response(support_request.message_id, support_request.response)
        return {"status": "Done"}
    except Exception as e:
        return {"status": "Error", "message": str(e)}

@router.post("/support")
async def create_support(support_request: SupportRequest):
    try:
        support_service.create_support(support_request.user_id)
        return {"status": "Done"}
    except Exception as e:
        return {"status": "Error", "message": str(e)}

@router.get("/support/{support_id}/message")
async def get_support_messages(support_id: int, processed: Optional[int]=0):
    try:
        return support_service.get_support_messages(support_id, processed=processed)
    except Exception as e:
        return {"status": "Error", "message": str(e)}

@router.get("/message")
async def get_support_messages():
    try:
        return support_service.get_messages()
    except Exception as e:
        return {"status": "Error", "message": str(e)}