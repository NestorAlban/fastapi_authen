import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import List
from typing import Optional
from typing import Final
from datetime import datetime
from app.usercase.get_all_active_users_usercase import AllActiveUserGetter
from app.schemas.user import UserCleanData

router = APIRouter()

GET_ALL_ACTIVE_USERS_ERROR_MESSAGE: Final = "ERROR IN get all active users ENDPOINT"
ALL_ACTIVE_USERS_ENDPOINT_SUMMARY: Final = "Show all active Users"
ALL_ACTIVE_USERS_ENDPOINT_PATH: Final = "/active_users"


@router.get(
    path=ALL_ACTIVE_USERS_ENDPOINT_PATH,
    response_model=List[UserCleanData],
    status_code=status.HTTP_200_OK,
    summary=ALL_ACTIVE_USERS_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def get_all_active_users():
    all_active_users_response = []
    try:
        all_active_user_getter = AllActiveUserGetter()
        users = all_active_user_getter.run()
        all_active_users_response = [UserCleanData(**user.__dict__) for user in users]
    except Exception as error:
        logging.error(GET_ALL_ACTIVE_USERS_ERROR_MESSAGE, error)
    return all_active_users_response