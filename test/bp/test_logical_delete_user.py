import pytest
from app.usercase import (
    UserDeactivator
)
from app.schemas import UserInfoBack, UpdateUser, UserCleanData, UserId
from app.database import DataBase
from app.models import User
from app.database import DataBase
from app.services import UserService
EXAMPLE_NAME = "Example"
EXAMPLE_EMAIL = "example@example.com"
EXAMPLE_PASSWORD = "example_password"
def test_update_user(create_user):
    db = DataBase()
    user_service = UserService()
    # user_creator = UserCreator()
    user_created = create_user(
        EXAMPLE_NAME, 
        EXAMPLE_EMAIL, 
        EXAMPLE_PASSWORD
    )
    # user = db.session.query(User).filter(User.id==user_created.id).first()
    
    user = user_service.get_user_id(user_created.id)
    assert user is not None
    assert user.name == EXAMPLE_NAME
    print('===========first user=================')
    print(
        user,
        '\n', 
    )
    response_1 = UserCleanData.construct(
        id = user.id,
        name = user.name,
        email = user.email,
        # password = user.password,
        is_active = user.is_active,
        status = user.status,
        role = user.role,
        created_at = user.created_at,
        updated_at = user.updated_at,
    ).dict(by_alias=True)
    print('===========first response=================')
    print(
        response_1,
        '\n', 
    )
    user_deactivator = UserDeactivator()
    user_de = user_deactivator.run(UserId(id=user.id))
    new_user = user_service.get_user_id(user_de.id)
    print('===========second user=================')
    print(
        new_user,
        new_user.id,
        '\n', 
    )
    response_2 = UserCleanData.construct(
        id = new_user.id,
        name = new_user.name,
        email = new_user.email,
        # password = new_user.password,
        is_active = new_user.is_active,
        status = new_user.status,
        role = new_user.role,
        created_at = new_user.created_at,
        updated_at = new_user.updated_at,
    ).dict(by_alias=True)
    print('===========second response=================')
    print(
        response_2,
        '\n', 
    )
    assert new_user is not None
    assert new_user.is_active == False
    user_service.delete_user_id(new_user.id)