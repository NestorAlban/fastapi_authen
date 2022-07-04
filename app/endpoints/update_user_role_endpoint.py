import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import Query, status
from fastapi import APIRouter
from fastapi import Path, Form
from fastapi import HTTPException
from typing import Any
from typing import Final
from typing import Dict
from typing import Optional
from datetime import datetime

from app.usercase import UserRoleUpdate
from app.schemas import UpdateUserRole, UserCleanData, RolesNum
from app.database import Mapping_rath


router = APIRouter()

UPDATE_USER_ROLE_ERROR_MESSAGE: Final = "ERROR IN update_user_role ENDPOINT"
UPDATE_USER_ROLE_ENDPOINT_SUMMARY: Final = "Update User's role"
UPDATE_USER_ROLE_ENDPOINT_PATH: Final = "/user/{id}/role"
SUCCESS_KEY: Final = "success"
USER_KEY: Final = "user"


@router.put(
    path=UPDATE_USER_ROLE_ENDPOINT_PATH,
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, Any],
    summary=UPDATE_USER_ROLE_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def update_user_role(
    # new_user_data: UpdateUserRole,
    ids: int,
    roles: int,
    # new_user_data_2: RolesNum
):
    success = False
    user_response = None
    print("=========================1")
    try:
        print("=========================2")
        user_update = UserRoleUpdate()
        # role = new_user_data.role
        role = roles
        if type(role) == int and role < 5:
            print("=========================3")
            users = user_update.run(UpdateUserRole(
                id = ids, 
                role = roles
            ))

            if users:
                print("=========================4")
                success = True
                #if users_response used just replace the user_response with it in the response
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
                new_role = Mapping_rath.role_mapping(user_response.get('role'))
                print("=========================",
                    new_role,
                    "========================="
                )
                user_response.update({'role': new_role})
        else:
            raise HTTPException(
                    status_code = status.HTTP_404_NOT_FOUND,
                    detail = f"Please write a number"
                )
    except Exception as error:
        logging.error(UPDATE_USER_ROLE_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, USER_KEY: user_response}