from typing import Optional
from datetime import datetime

from dataclasses import dataclass

@dataclass(frozen=True)
class UserDomaint:
    id: int
    name: str
    email: str
    password: str
    is_active: Optional[bool]
    status: int 
    role: int 
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class Domain:
    def __init__(self) -> None:
        pass

    @staticmethod
    def create_user_domain(user):
        #you can use the UserDomain in this file or UserDomaint in domain.py file in this folder
        user_domain = UserDomaint(
            user.id, 
            user.name, 
            user.email, 
            user.password,
            user.is_active, 
            user.status,
            user.role,
            user.created_at,
            user.updated_at
        )
        return user_domain