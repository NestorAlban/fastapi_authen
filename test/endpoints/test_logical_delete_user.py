import pytest
from app.usercase import (
    UserDeactivator
)
from app.schemas import UserInfoBack, UpdateUser, UserCleanData, UserId
from app.database import DataBase
from app.models import User
from app.database import DataBase
from app.services import UserService
from fastapi.testclient import TestClient
EXAMPLE_NAME = "Example"
EXAMPLE_EMAIL = "example@example.com"
EXAMPLE_PASSWORD = "example_password"
def test_update_user(app, create_user):
    db = DataBase()
    user_service = UserService()
    user_created = create_user(
        EXAMPLE_NAME, 
        EXAMPLE_EMAIL, 
        EXAMPLE_PASSWORD
    )
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
        user.id
    )
    client = TestClient(app)
    response = client.delete(
        "/user/deactivate",
        json={
            "id": user.id,
        }
    ).json()
    print('==============response===================')
    print(response)
    # new_user = response.get('user')
    # print('===========second user=================')
    # print(
    #     new_user,
    #     new_user.get('id'),
    #     '\n', 
    # )
    assert response is not None
    # assert new_user.get('id') == user.id
    # assert new_user.get('name') == EXAMPLE_NAME
    # assert new_user.get('email') == EXAMPLE_EMAIL
    # assert new_user.get('is_active') == False
    user_service.delete_user_id(user.id)

    