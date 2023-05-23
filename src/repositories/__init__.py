from core_repository.user_repository import UserRepository
from core_repository.admin_repository import AdminRepository
from .support_repository import SupportRepository
from .message_repository import MessageRepository
from ..config import DSN

user_repository: UserRepository = UserRepository(DSN)
admin_repository: AdminRepository = AdminRepository(DSN)
support_repository: SupportRepository = SupportRepository(DSN)
message_repository: MessageRepository = MessageRepository(DSN)