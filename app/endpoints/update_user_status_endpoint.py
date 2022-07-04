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

from app.usercase import UserStatusUpdate
from app.schemas import UpdateUserStatus, UserCleanData


router = APIRouter()

UPDATE_USER_STATUS_ERROR_MESSAGE: Final = "ERROR IN update_user_status ENDPOINT"
UPDATE_USER_STATUS_ENDPOINT_SUMMARY: Final = "Update User's status"
UPDATE_USER_STATUS_ENDPOINT_PATH: Final = "/user/{id}/status"
SUCCESS_KEY: Final = "success"
USER_KEY: Final = "user"


@router.put(
    path=UPDATE_USER_STATUS_ENDPOINT_PATH,
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, Any],
    summary=UPDATE_USER_STATUS_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def update_user_status(new_user_data: UpdateUserStatus):
    success = False
    users_response = None
    try:
        user_update = UserStatusUpdate()
        status = new_user_data.status
        if type(status) == int:
            users = user_update.run(UpdateUserStatus(
                id=new_user_data.id, 
                status = new_user_data.status
            ))
            if users:
                success = True
                users_response = UserCleanData(**users.__dict__)
    except Exception as error:
        logging.error(UPDATE_USER_STATUS_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, USER_KEY: users_response}