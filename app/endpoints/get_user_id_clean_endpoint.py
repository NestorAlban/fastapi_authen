import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import Path
from fastapi import status
from fastapi import APIRouter
from typing import Dict
from typing import Optional
from typing import Final
from typing import Any

from datetime import datetime

from app.usercase.get_user_id_clean_usercase import OneCleanUserGetter
from app.schemas import UserId, UserCleanData


router = APIRouter()

GET_ONE_CLEAN_USER_ERROR_MESSAGE: Final = "ERROR IN one clean user ENDPOINT"
ONE_CLEAN_USER_ENDPOINT_SUMMARY: Final = "Show one clean User"
ONE_CLEAN_USER_ENDPOINT_PATH: Final = "/user/c/{id}"
USER_KEY: Final = "user"

@router.get(
    path=ONE_CLEAN_USER_ENDPOINT_PATH,
    response_model=Dict[str, Any],
    status_code=status.HTTP_200_OK,
    summary=ONE_CLEAN_USER_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def get_one_clean_user(id: int = Path(
    ..., 
    title="User ID"
)):
    one_user_response = None
    try:
        one_user_getter = OneCleanUserGetter()
        one_user = one_user_getter.run(UserId(
            id = id
        ))
        if one_user:
            one_user_response = UserCleanData(
                **one_user.__dict__
            )
    except Exception as error:
        logging.error(
            GET_ONE_CLEAN_USER_ERROR_MESSAGE,
            error
        )
    return {USER_KEY: one_user_response}