import pytest
from app.usercase import UserCreator
from app.schemas import UserInfoBack
from app.database import DataBase
from app.models import User
from app.database import DataBase
from app.services import UserService
EXAMPLE_NAME = "Example"
def test_create_user():
    db = DataBase()
    user_creator = UserCreator()
    user_created = user_creator.run(UserInfoBack(
        name = EXAMPLE_NAME,
        email= "example_email",
        password= "example_password"
    ))
    # user = db.session.query(User).filter(User.id==user_created.id).first()
    user_service = UserService()
    user = user_service.get_user_id(user_created.id)
    print('============================')
    print(user)

    assert user is not None
    assert user.name == EXAMPLE_NAME
    user_service.delete_user_id(user.id)
    # db.session.delete(user)
    # db.session.commit()
# get all con assert de len 
# get 1 con filter
# update
# delete
