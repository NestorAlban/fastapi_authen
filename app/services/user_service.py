from app.models import User
from app.database import UserDomain
from app.database import DataBase

from typing import List


class UserService:
    def __init__(self):
        self.alchemy_db = DataBase()
        pass

    def login_user(
        self, 
        name: str, 
        password: str
    ):
        user = self.alchemy_db.login_user(
            name, 
            password
        )
        return user

    def create_user(
        self, 
        name: str, 
        email: str, 
        password: str
    ) -> UserDomain:
        user = self.alchemy_db.create_user(
            name, 
            email, 
            password
        )
        return user
    
    def delete_user_id(
        self, 
        id: int
    ):
        user = self.alchemy_db.delete_user_id(id)
        return user

    def get_user_id(
        self, 
        id: int
    ):
        user = self.alchemy_db.get_user_id(id)
        return user

    def get_all_users(self):
        users = []
        users = self.alchemy_db.get_all_users()
        return users

    def get_all_active_users(self):
        users = []
        users = self.alchemy_db.get_all_active_users()
        return users

    def change_user_password(
        self, 
        email: str
    ):
        user = self.alchemy_db.change_user_password(email)
        return user
        
    def update_user(
        self, 
        id: int, 
        name: str, 
        email: str
    ):
        users = self.alchemy_db.update_user(
            id, 
            name, 
            email
        )
        return users

    def deactivate_user(
        self, 
        id: int
    ):
        users = self.alchemy_db.deactivate_user(id)
        return users

    def activate_user(
        self, 
        id: int
    ):
        users = self.alchemy_db.activate_user(id)
        return users

    def update_user_role(
        self, 
        id: int, 
        role: int
    ):
        users = self.alchemy_db.update_user_role(
            id, 
            role,
        )
        return users

    def update_user_status(
        self, 
        id: int, 
        status: int
    ):
        users = self.alchemy_db.update_user_status(
            id, 
            status,
        )
        return users

    