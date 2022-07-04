import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import Any
from typing import Final
from typing import Dict
from typing import Optional
from datetime import datetime

from app.usercase import UserUpdate
from app.schemas import UpdateUser, UserCleanData


router = APIRouter()

UPDATE_USER_ERROR_MESSAGE: Final = "ERROR IN update_user ENDPOINT"
UPDATE_USER_ENDPOINT_SUMMARY: Final = "Update a new User"
UPDATE_USER_ENDPOINT_PATH: Final = "/user/{id}/update_user"
SUCCESS_KEY: Final = "success"
USER_KEY: Final = "user"


@router.put(
    path=UPDATE_USER_ENDPOINT_PATH,
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, Any],
    summary=UPDATE_USER_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def update_user(new_user_data: UpdateUser):
    success = False
    users_response = None
    try:
        user_update = UserUpdate()
        name = new_user_data.name.strip()
        email = new_user_data.email.strip()
        if len(name) != 0 and len(email) != 0:
            users = user_update.run(UpdateUser(
                id=new_user_data.id, 
                name=name, 
                email=email
            ))
            if users:
                success = True
                users_response = UserCleanData(**users.__dict__)
    except Exception as error:
        logging.error(UPDATE_USER_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, USER_KEY: users_response}
