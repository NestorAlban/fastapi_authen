from pydantic import BaseModel
from pydantic import Field
from fastapi import Path, Query
from typing import List, Optional
from datetime import datetime

class CompanyData(BaseModel):
    id: int 
    name: str = Field(default = "Example_company")
    status: Optional[int] = Field(default = 0)
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()

class CompanyName(BaseModel):
    name: str = Field(default = "Example_company")

class CompanyId(BaseModel):
    id: int 