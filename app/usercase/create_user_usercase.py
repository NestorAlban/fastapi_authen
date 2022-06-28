from app.services import UserService
from pydantic import Field, BaseModel
from app.database.database import UserDomain
from app.schemas import UserInfoBack



class UserCreator:
    def __init__(self):
        UserInfoBack
        pass

    def run(self, params: UserInfoBack) -> UserDomain:
        user_service = UserService()
        user = user_service.create_user(
            params.name,
            params.email,
            params.password
        )
        print("==============success1============")
        return user