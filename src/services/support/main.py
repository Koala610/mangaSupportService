from src.repositories import SupportRepository, MessageRepository
from src.models.user import User, Support, Message
class SupportService:
    def __init__(self, support_repository: SupportRepository, message_repository: MessageRepository):
        self.support_repository = support_repository
        self.message_repository = message_repository

    def get_messages(self):
        return self.message_repository.find_all()

    def get_message(self, message_id):
        return self.message_repository.find_by_id(message_id)

    def get_message_by_processed(self, processed):
        return self.message_repository.find_message_by_processed(processed=processed)

    def get_support_messages(self, support_id, processed: int):
        messages = self.support_repository.get_messages(support_id)
        if (processed == 0):
            return messages
        if (processed == 1):
            return [i for i in messages if i.is_processed == True]
        if (processed == -1):
            return [i for i in messages if i.is_processed == False]

    def create_message(self, user_id, message):
        self.message_repository.create(user_id=user_id, message=message)

    def set_message_support(self, message_id, support_id):
        self.message_repository.update(message_id, support_id=support_id)

    def set_message_response(self, support_id, message_id, response):
        self.message_repository.update(message_id, is_processed=True, response=response, support_id=support_id)

    def create_support(self, message_id, response):
        self.message_repository.update(message_id, is_processed=True, response=response)

    def create_support(self, user_id):
        self.support_repository.create(user_id=user_id)

    def get_messages_in_range(self, offset, limit):
        return self.message_repository.find_in_range(offset, limit)

    def get_messages_count(self):
        return self.message_repository.count()