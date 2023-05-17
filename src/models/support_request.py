from pydantic import BaseModel
from typing import Optional

class SupportRequest(BaseModel):
    support_id: Optional[int]
    message: Optional[str]
    message_id: Optional[str]
    user_id: Optional[int]
    response: Optional[str]