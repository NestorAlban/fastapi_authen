from enum import Enum
from pydantic import BaseModel
from pydantic import Field
from fastapi import Path, Query
from typing import Optional
from datetime import datetime

class VendorData(BaseModel):
    id: int 
    name: Optional[int] = Field(default = 1)
    status: Optional[int] = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()


