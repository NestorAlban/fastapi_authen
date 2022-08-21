import pytest
from app.usercase import (
    UserUpdate
)
from app.schemas import UserInfoBack, UpdateUser, UserCleanData
from app.database import DataBase
from app.models import User
from app.database import DataBase
from app.services import UserService
from fastapi.testclient import TestClient
EXAMPLE_NAME = "Example"
EXAMPLE_EMAIL = "example@example.com"
EXAMPLE_PASSWORD = "example_password"
NEW_EXAMPLE_NAME = "New Example"
NEW_EXAMPLE_EMAIL = "new_example@example.com"
def test_update_user(app, create_user):
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
    client = TestClient(app)
    response = client.put(
        "/user/{}/update_user".format(user.id),
        json={
            "id": user.id,
            "name": NEW_EXAMPLE_NAME,
            "email": NEW_EXAMPLE_EMAIL,
        }
    ).json()
    print('==============response===================')
    print(response)
    new_user = response.get('user')
    print('===========second user=================')
    print(
        new_user,
        new_user.get('id'),
        '\n', 
    )
    assert response
    assert new_user.get('id') == user.id
    assert new_user.get('name') == NEW_EXAMPLE_NAME
    assert new_user.get('email') == NEW_EXAMPLE_EMAIL
    user_service.delete_user_id(user.id)