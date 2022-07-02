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

from app.usercase.change_user_password_usercase import EmailUserGetter
from app.schemas import UserId, UserCleanData, UserEmailDefault


router = APIRouter()

CHANGE_USER_PASSWORD_ERROR_MESSAGE: Final = "ERROR IN change user password ENDPOINT"
CHANGE_USER_PASSWORD_ENDPOINT_SUMMARY: Final = "Change User password"
CHANGE_USER_PASSWORD_ENDPOINT_PATH: Final = "/change_password"
USER_KEY: Final = "user"
CODE_KEY: Final = "reset_code"

@router.post(
    path=CHANGE_USER_PASSWORD_ENDPOINT_PATH,
    response_model=Dict[str, Any],
    status_code=status.HTTP_200_OK,
    summary=CHANGE_USER_PASSWORD_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def change_user_password(user_email: UserEmailDefault):
    one_user_response = None
    one_user_data = None
    one_user_code = None
    try:
        print("Email>error end 1")
        one_user_email_getter = EmailUserGetter()
        one_user = one_user_email_getter.run(UserEmailDefault(
            email = user_email.email
        ))
        if one_user:
            one_user_data = one_user.get('user')
            one_user_code = one_user.get('reset_code')
            print("Email>error end 3")
            one_user_response = UserCleanData(
                **one_user_data.__dict__
            )
            # print(one_user_response)
            print("Email>error end 4")
    except Exception as error:
        logging.error(
            CHANGE_USER_PASSWORD_ERROR_MESSAGE,
            error
        )
    return {
        USER_KEY: one_user_response, 
        CODE_KEY: one_user_code
    }