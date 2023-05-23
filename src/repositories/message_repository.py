from core_repository.crud_repository import CRUDRepository
from core_entity.user import Message
from src.logger import logger

class MessageRepository(CRUDRepository):
    def __init__(self, dsn: str):
        super().__init__(Message, dsn)
        logger.info("MessageRepository initialized...")

    def find_message_by_processed(self, processed):
        with self.Session() as session:
            return session.query(self.Object).filter_by(is_processed=processed).all()
