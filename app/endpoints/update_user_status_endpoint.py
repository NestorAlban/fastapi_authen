
import logging
import fastapi
from pydantic import BaseModel
from pydantic import Field
from fastapi import Query, status
from fastapi import APIRouter
from fastapi import HTTPException
from typing import Any
from typing import Final
from typing import Dict
from typing import Optional
from datetime import datetime

from app.usercase import UserStatusUpdate
from app.schemas import UpdateUserStatus, UserCleanData
from app.database import Mapping_rath


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
def update_user_status(
    # new_user_data: UpdateUserStatus,
    id: int,
    stat: int
):
    success = False
    users_response = None
    try:
        user_update = UserStatusUpdate()
        status = stat
        if type(stat) == int and stat < 4:
            users = user_update.run(UpdateUserStatus(
                id= id, 
                status = stat
            ))
            if users:
                success = True
                users_response = UserCleanData(**users.__dict__)
                user_response = UserCleanData.construct(
                    id = users.id,
                    name = users.name,
                    email = users.email,
                    is_active = users.is_active,
                    status = users.status,
                    role = users.role,
                    created_at = users.created_at,
                    updated_at = users.updated_at,
                ).dict(by_alias=True)
                print("=========================",
                    user_response, 
                    user_response.get('role'), 
                    type(user_response),
                    "========================="
                )
                new_status = Mapping_rath.status_mapping(user_response.get('status'))
                role_name = Mapping_rath.role_mapping(user_response.get('role'))
                print("=========================",
                    new_status,
                    "========================="
                )
                user_response.update({'role': role_name})
                user_response.update({'status': new_status})
        else:
            raise HTTPException(
                    status_code = fastapi.status.HTTP_404_NOT_FOUND,
                    detail = f"Please write a number"
                )
    except Exception as error:
        logging.error(UPDATE_USER_STATUS_ERROR_MESSAGE, error)     
    return {SUCCESS_KEY: success, USER_KEY: user_response}