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
        support_service.set_message_response(support_request.support_id, support_request.message_id, support_request.response)
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
async def get_messages(offset: Optional[int] = None, limit:Optional[int] = None):
    try:
        if offset is not None and limit is not None:
            return support_service.get_messages_in_range(offset=offset, limit=limit)
        return support_service.get_messages()
    except Exception as e:
        return {"status": "Error", "message": str(e)}

@router.get("/message/unprocessed")
async def get_unprocessed_messages():
    try:
        return support_service.get_message_by_processed(False)
    except Exception as e:
        return {"status": "Error", "message": str(e)}

@router.get("/message/processed")
async def get_processed_messages():
    try:
        return support_service.get_message_by_processed(True)
    except Exception as e:
        return {"status": "Error", "message": str(e)}

@router.get("/message/{id}")
async def get_message(id: int):
    try:
        return support_service.get_message(id)
    except Exception as e:
        return {"status": "Error", "message": str(e)}

@router.get("/message/count")
async def get_support_messages():
    try:
        return support_service.get_messages_count()
    except Exception as e:
        return {"status": "Error", "message": str(e)}

@router.get("/support/get")
async def get_support(user_id: int):
    try:
        return support_service.get_support_by_user_id(user_id)
    except Exception as e:
        return {"status": "Error", "message": str(e)}