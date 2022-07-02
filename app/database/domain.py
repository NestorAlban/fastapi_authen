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
    created_at: Optional[datetime]
    updated_at: Optional[datetime]