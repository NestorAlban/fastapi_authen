from enum import Enum
from pydantic import BaseModel
from pydantic import Field
from fastapi import Path, Query
from typing import List, Optional
from datetime import datetime

class SellID(BaseModel):
    id: int 

class Sell(BaseModel):
    id: int 
    user: int
    product: int

class SellData(BaseModel):
    id: int 
    user: int = Field()
    product: int = Field()
    status: Optional[int] = Field()
    payment: Optional[int] = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()

class SellInfoBack(BaseModel):
    user: int = Field()
    product: int = Field()

class SellID(BaseModel):
    id: int 
