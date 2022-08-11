from enum import Enum
from pydantic import BaseModel
from pydantic import Field
from fastapi import Path, Query
from typing import Optional
from datetime import datetime

class EnrollmentData(BaseModel):
    id: int 
    user: Optional[int] = Field(default = 1)
    vendor: Optional[int] = Field(default = 1)
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()

class EnrollmentInfoBack(BaseModel):
    user: Optional[int] = Field(default = 1)
    vendor: Optional[int] = Field(default = 1)