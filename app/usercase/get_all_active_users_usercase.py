from app.services import UserService
from typing import List
from app.models import User


class AllActiveUserGetter:
    def __init__(self):
        pass

    def run(self) -> List[User]:
        users = []
        user_service = UserService()
        users = user_service.get_all_active_users()
        return users