from enum import Enum
from pydantic import BaseModel
from pydantic import Field
from fastapi import Path, Query
from typing import Optional
from datetime import datetime

class UserId(BaseModel):
    id: int = Field(...)

class UserIdDefault(BaseModel):
    id: int = Field(default = 1)

class UserEmailDefault(BaseModel):
    email: str = Field(default = "example@email.com")

class UserInfoBack(BaseModel):
    name: str = Field(default = "Example_username")
    email: str = Field(default = "example@email.com")
    password: str = Field(default = "Example_password")

class UpdateUser(BaseModel):
    id: int = Field(default = 1)
    name: str = Field(default = "Example_username")
    email: str = Field(default = "example@email.com")

class UpdateUserRole(BaseModel):
    id: int = Field(default = 1)
    role: int = Field(default = 0)

class UpdateUserStatus(BaseModel):
    id: int = Field(default = 1)
    status: int = Field(default = 1)

class RolesNum(BaseModel):
    # id: int = Path(
    # ..., 
    # title="User ID"
    #     )
    role: int = Query(
        ...,
        lt = 5,
        # examples = {
        #     "role1": 0,
        #     "role2": 1,
        #     "role3": 2,
        # },
    )

class UserData(BaseModel):
    id: int 
    name: str = Field(default = "Example_username")
    email: str = Field(default = "example@email.com")
    password: str = Field(default = "Example_password")
    is_active: Optional[bool] = Field()
    status: Optional[int] = Field()
    role: Optional[int] = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()

class UserCleanData(BaseModel):
    id: int 
    name: str = Field(default = "Example_username")
    email: str = Field(default = "example@email.com")
    is_active: Optional[bool] = Field()
    status: Optional[int] = Field()
    role: Optional[int] = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()
