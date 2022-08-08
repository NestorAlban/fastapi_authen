import pytest
from app.usercase import UserCreator
from app.schemas import UserInfoBack
from app.database import DataBase
from app.models import User

def test_create_user():
    db = DataBase()
    user_creator = UserCreator()
    user = user_creator.run(UserInfoBack(
        name = "Example",
        email= "example_email",
        password= "example_password"
    ))
    print("================1")
    print(user)

    assert user is not None