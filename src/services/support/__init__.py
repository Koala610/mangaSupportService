from .main import SupportService
from src.repositories import support_repository, message_repository

support_service = SupportService(support_repository, message_repository)