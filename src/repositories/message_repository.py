from .crud_repository import CRUDRepository
from src.models.user import Message
from src.logger import logger

class MessageRepository(CRUDRepository):
    def __init__(self, dsn: str):
        super().__init__(Message, dsn)
        logger.info("MessageRepository initialized...")
