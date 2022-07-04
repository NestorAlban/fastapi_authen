from app.services import UserService
from typing import List
from app.models import User
from pydantic import Field
from pydantic import BaseModel
from app.schemas import UpdateUserRole


class UserRoleUpdate:
    def __init__(self):
        pass

    def run(self, params: UpdateUserRole):
        user_service = UserService()
        users = user_service.update_user_role(
            params.id, 
            params.role
        )
        return users