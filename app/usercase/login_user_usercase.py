from app.services import UserService
from app.models import User
from pydantic import Field
from app.schemas import LoginData, UserCleanData

class LoginUser:
    def __init__(self):
        LoginData
        pass

    def run(self, params: LoginData) -> User:
        user_service = UserService()
        user = user_service.login_user(
            params.name, 
            params.password
        )
        print("============================")
        print(user)
        d = user.get('user')
        if d != None:
            login_user_response = UserCleanData(
                **d.__dict__
            )
            print(user.get('user'))
            print(login_user_response)
            print("============================")
        return user