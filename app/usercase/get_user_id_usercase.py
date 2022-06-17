from app.services import UserService
from app.models import User
from pydantic import Field
from app.schemas import UserId

class OneUserGetter:
    def __init__(self):
        UserId
        pass

    def run(self, params: UserId) -> User:
        user_service = UserService()
        user = user_service.get_user_id(params.id)
        return user
