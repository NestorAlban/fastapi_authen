import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import Path
from fastapi import status
from fastapi import APIRouter
from typing import Any
from typing import Optional
from typing import Final
from typing import Dict

from datetime import datetime

from app.schemas import UserId, UserCleanData
from app.usercase import UserDeactivator


router = APIRouter()

DEACTIVATE_USER_ERROR_MESSAGE: Final = "ERROR IN deactivate_user ENDPOINT"
DEACTIVATE_USER_ENDPOINT_SUMMARY: Final = "Deactivate User"
DEACTIVATE_USER_ENDPOINT_PATH: Final = "/user/deactivate/{id}"
SUCCESS_KEY: Final = "success"
USER_KEY: Final = "user"


@router.delete(
    path=DEACTIVATE_USER_ENDPOINT_PATH,
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, Any],
    summary=DEACTIVATE_USER_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def activate_user(id: int):
    success = False
    user_response = None
    try:
        user_getter = UserDeactivator()
        user = user_getter.run(UserId(id=id))
        if user:
            # success = True
            # user_response = UserCleanData.construct(**user.__dict__)
            user_response = UserCleanData.construct(
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
            success = True
    except Exception as error:
        logging.error(DEACTIVATE_USER_ERROR_MESSAGE, error)

    return {SUCCESS_KEY: success, USER_KEY: user_response}
