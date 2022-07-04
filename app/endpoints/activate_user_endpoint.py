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
from app.usercase import UserActivator


router = APIRouter()

ACTIVATE_USER_ERROR_MESSAGE: Final = "ERROR IN activate_user ENDPOINT"
ACTIVATE_USER_ENDPOINT_SUMMARY: Final = "Activate User"
ACTIVATE_USER_ENDPOINT_PATH: Final = "/user/activate"
SUCCESS_KEY: Final = "success"
USER_KEY: Final = "user"


@router.put(
    path=ACTIVATE_USER_ENDPOINT_PATH,
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, Any],
    summary=ACTIVATE_USER_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def activate_user(id: int):
    success = False
    user_response = None
    try:
        user_getter = UserActivator()
        user = user_getter.run(UserId(id=id))
        if user:
            success = True
            user_response = UserCleanData.construct(**user.__dict__)
    except Exception as error:
        logging.error(ACTIVATE_USER_ERROR_MESSAGE, error)

    return {SUCCESS_KEY: success, USER_KEY: user_response}
