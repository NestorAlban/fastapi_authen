import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import List
from typing import Optional
from typing import Final
from datetime import datetime
from app.usercase.get_all_users_usercase import AllUserGetter
from app.schemas.user import UserData

router = APIRouter()

GET_ALL_USERS_ERROR_MESSAGE: Final = "ERROR IN get all users ENDPOINT"
ALL_USERS_ENDPOINT_SUMMARY: Final = "Show all Users"
ALL_USERS_ENDPOINT_PATH: Final = "/all_users"


@router.get(
    path=ALL_USERS_ENDPOINT_PATH,
    response_model=List[UserData],
    status_code=status.HTTP_200_OK,
    summary=ALL_USERS_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def get_all_users():
    all_users_response = []
    try:
        all_user_getter = AllUserGetter()
        users = all_user_getter.run()
        all_users_response = [UserData(**user.__dict__) for user in users]
    except Exception as error:
        logging.error(GET_ALL_USERS_ERROR_MESSAGE, error)
    return all_users_response
