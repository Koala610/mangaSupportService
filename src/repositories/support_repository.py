from .crud_repository import CRUDRepository
from src.models.user import Support
from src.logger import logger

class SupportRepository(CRUDRepository):
    def __init__(self, dsn: str):
        super().__init__(Support, dsn)
        logger.info("SupportRepository initialized...")

    def get_messages(self, id):
        with self.Session() as session:
            support: Support = session.query(self.Object).get(id)
            if support is None:
                raise Exception(f"No support with id {id}")
            return support.messages

    def find_by_user_id(self, user_id: int):
        with self.Session() as session:
            support: Support = session.query(self.Object).filter_by(user_id = user_id).first()
            if support is None:
                raise Exception(f"No support with id {id}")
            return support
