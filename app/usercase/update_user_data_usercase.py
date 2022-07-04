from app.services import UserService
from typing import List
from app.models import User
from pydantic import Field
from pydantic import BaseModel
from app.schemas import UpdateUser


class UserUpdate:
    def __init__(self):
        pass

    def run(self, params: UpdateUser):
        user_service = UserService()
        users = user_service.update_user(params.id, params.name, params.email)
        return users
