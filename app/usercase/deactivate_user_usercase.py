from app.services import UserService
from pydantic import Field
from pydantic import BaseModel
from app.database import UserDomain
from app.schemas import UserId



class UserDeactivator:
    def __init__(self):
        pass

    def run(self, params: UserId) -> UserDomain:
        user_service = UserService()
        user = user_service.deactivate_user(params.id)
        return user
