from enum import Enum
from pydantic import BaseModel
from pydantic import Field
from fastapi import Path, Query
from typing import Optional
from datetime import datetime


class ProductInfoBack(BaseModel):
    name: str = Field(default = "Example_product")
    branch: str = Field(default = "saga")

class ProductData(BaseModel):
    id: int 
    name: str = Field(default = "Example_product")
    branch: str = Field(default = "saga")
    amount: int = Field(default = 0)
    available: Optional[bool] = Field()
    status: Optional[int] = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()