from app.services import UserService
from app.models import User
from pydantic import Field
from app.schemas import UserEmailDefault

class EmailUserGetter:
    def __init__(self):
        # UserId
        pass

    def run(self, params: UserEmailDefault) -> User:
        user_service = UserService()
        user = user_service.change_user_password(params.email)
        return user