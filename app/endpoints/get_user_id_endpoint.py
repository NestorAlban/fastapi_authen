import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import Path, Depends
from fastapi import status
from fastapi import APIRouter
from typing import Dict
from typing import Optional
from typing import Final
from typing import Any

from datetime import datetime

from app.usercase.get_user_id_usercase import OneUserGetter
from app.schemas import UserId, UserData
from app.database import GetCurrentUsers


router = APIRouter()

GET_ONE_USER_ERROR_MESSAGE: Final = "ERROR IN one user ENDPOINT"
ONE_USER_ENDPOINT_SUMMARY: Final = "Show one User"
ONE_USER_ENDPOINT_PATH: Final = "/user/{id}"
USER_KEY: Final = "user"

@router.get(
    path=ONE_USER_ENDPOINT_PATH,
    response_model=Dict[str, Any],
    status_code=status.HTTP_200_OK,
    summary=ONE_USER_ENDPOINT_SUMMARY,
    tags=["Users"],
)
def get_one_user(id: int = Path(
    ..., 
    title="User ID"
    ),
    get_current_user: UserData = Depends(GetCurrentUsers.get_current_user)
):
    one_user_response = None
    try:
        one_user_getter = OneUserGetter()
        one_user = one_user_getter.run(UserId(id = id))
        if one_user:
            one_user_response = UserData(**one_user.__dict__)
            one_user_response = UserData.construct(
                id = one_user.id,
                name = one_user.name,
                email = one_user.email,
                password = one_user.password,
                is_active = one_user.is_active,
                status = one_user.status,
                role = one_user.role,
                created_at = one_user.created_at,
                updated_at = one_user.updated_at,
            ).dict(by_alias=True)
    except Exception as error:
        logging.error(GET_ONE_USER_ERROR_MESSAGE, error)
    return {USER_KEY: one_user_response}
