import logging
from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from typing import Final

from app.schemas import (
    LoginData, 
    UserCleanData,
    UserData
) 

from app.usercase import LoginUser

router = APIRouter()

LOGIN_USER_ERROR_MESSAGE: Final = "ERROR IN login user ENDPOINT"
LOGIN_USER_ENDPOINT_SUMMARY: Final = "Login a User"
LOGIN_USER_ENDPOINT_PATH: Final = "/login"
USER_KEY: Final = "user"
TOKEN_KEY: Final = "access_token"
TOKEN_TYPE_KEY: Final = "token_type"

@router.post(
    path=LOGIN_USER_ENDPOINT_PATH,
    status_code=status.HTTP_200_OK,
    summary=LOGIN_USER_ENDPOINT_SUMMARY,
    tags=["Authentication"],
)
def login_user(login_user_data: OAuth2PasswordRequestForm = Depends()):
    login_user_response = None
    login_user_token_value = None
    login_user_token_type = None
    try:
        login_user_getter = LoginUser()
        login_user = login_user_getter.run(LoginData(
            name = login_user_data.username,
            password = login_user_data.password
        ))
        if login_user:
            print("11111111============================11111")
            print(login_user)
            login_user_token = login_user.get('token')
            print(login_user_token)

            print("============================")
            login_user_data = login_user.get('user')
            if login_user_data:
                login_user_response = UserCleanData(
                    **login_user_data.__dict__
                )
                login_user_token_value = login_user_token[0]
                login_user_token_type = login_user_token[1]
    except Exception as error:
        logging.error(
            LOGIN_USER_ERROR_MESSAGE,
            error
        )
    return {
        USER_KEY: login_user_response,
        TOKEN_KEY: login_user_token_value,
        TOKEN_TYPE_KEY: login_user_token_type
    }
