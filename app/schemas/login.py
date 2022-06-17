from pydantic import BaseModel
from pydantic import Field
from typing import Optional
from datetime import datetime

class LoginData(BaseModel):
    name: str
    password: str