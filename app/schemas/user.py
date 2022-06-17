from pydantic import BaseModel
from pydantic import Field
from typing import Optional
from datetime import datetime

class UserId(BaseModel):
    id: int = Field(...)

class UserIdDefault(BaseModel):
    id: int = Field(default = 1)



class UserInfoBack(BaseModel):
    name: str = Field(default = "Example_username")
    email: str = Field(default = "example@email.com")
    password: str = Field(default = "Example_password")

class UserData(BaseModel):
    id: int 
    name: str = Field(default = "Example_username")
    email: str = Field(default = "example@email.com")
    password: str = Field(default = "Example_password")
    is_active: Optional[bool] = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()

class UserCleanData(BaseModel):
    id: int 
    name: str = Field(default = "Example_username")
    email: str = Field(default = "example@email.com")
    is_active: Optional[bool] = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()
