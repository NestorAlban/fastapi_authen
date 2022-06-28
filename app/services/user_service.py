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
        print(user)
        print("====================asd===========")
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
        print("==============success2============")
        return user
    
    def get_user_id(
        self, 
        id: int
    ):
        user = self.alchemy_db.get_user_id(id)
        return user
