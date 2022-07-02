import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import List
from typing import Optional
from typing import Final
from datetime import datetime
from app.usercase.get_all_users_clean_usercase import AllUserCleanGetter
from app.schemas.user import UserCleanData

router = APIRouter()

GET_ALL_CLEAN_USERS_ERROR_MESSAGE: Final = "ERROR IN get all clean users ENDPOINT"
ALL_CLEAN_USERS_ENDPOINT_SUMMARY: Final = "Show all clean Users"
ALL_CLEAN_USERS_ENDPOINT_PATH: Final = "/all_users/c"


@router.get(
    path=ALL_CLEAN_USERS_ENDPOINT_PATH,
    response_model=List[UserCleanData],
    status_code=status.HTTP_200_OK,
    summary=ALL_CLEAN_USERS_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def get_all_clean_users():
    all_clean_users_response = []
    try:
        all_clean_user_getter = AllUserCleanGetter()
        users = all_clean_user_getter.run()
        all_clean_users_response = [UserCleanData(**user.__dict__) for user in users]
    except Exception as error:
        logging.error(GET_ALL_CLEAN_USERS_ERROR_MESSAGE, error)
    return all_clean_users_response
