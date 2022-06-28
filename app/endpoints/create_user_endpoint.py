import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import Final
from typing import Optional
from datetime import datetime

from app.usercase.create_user_usercase import UserCreator
from app.schemas import UserData, UserInfoBack

router = APIRouter()

CREATE_USER_ERROR_MESSAGE: Final = "ERROR IN create_user ENDPOINT"
CREATE_USER_ENDPOINT_SUMMARY: Final = "Create a new User"
CREATE_USER_ENDPOINT_PATH: Final = "/create_user"
SUCCESS_KEY: Final = "success"
USER_KEY: Final = "user"

class CreateUserInput(UserInfoBack):
    pass

class UserResponse(UserData):
    pass

@router.post(
    path=CREATE_USER_ENDPOINT_PATH,
    status_code=status.HTTP_201_CREATED,
    summary=CREATE_USER_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def create_user(new_user_data: UserInfoBack):
    success = False
    user_response = None
    try:
        user_creator = UserCreator()
        name = new_user_data.name.strip()
        email = new_user_data.email.strip()
        password = new_user_data.password.strip()

        if len(name) != 0 and len(email) != 0 and len(password) != 0:
            user = user_creator.run(UserInfoBack(
                name = name, 
                email = email,
                password = password
                )
            )
            if user:
                user_response = UserResponse.construct(
                    id = user.id,
                    name = user.name,
                    email = user.email,
                    password = user.password,
                    is_active = user.is_active,
                    created_at = user.created_at,
                    updated_at = user.updated_at,
                ).dict(by_alias=True)
                success = True
                print("==============success============")
    except Exception as error:
        logging.error(CREATE_USER_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, USER_KEY: user_response}

