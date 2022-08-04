from enum import Enum
from pydantic import BaseModel
from pydantic import Field
from fastapi import Path, Query
from typing import List, Optional
from datetime import datetime

class ProductId(BaseModel):
    id: int 

class ProductName(BaseModel):
    name: str = Field(default = "Example_product")

class ProductBranch(BaseModel):
    branch: str = Field(default = "saga")

class ProductTag(BaseModel):
    tags: List[str] = Field(default = ["Tag1", "Tag2", "Tag3"])

class UpdateProductInfo(BaseModel):
    id: int 
    name: str = Field(default = "Example_product")
    branch: str = Field(default = "saga")
    description: str = Field(default = "New product")

class UpdateProductAmount(BaseModel):
    id: int 
    amount: int = Field(default = 0)

class ProductInfoBack(BaseModel):
    name: str = Field(default = "Example_product")
    branch: str = Field(default = "saga")
    description: str = Field(default = "New product")
    tags: List[str] = Field(default = ["Tag1", "Tag2", "Tag3"])

class ProductData(BaseModel):
    id: int 
    name: str = Field(default = "Example_product")
    branch: str = Field(default = "saga")
    description: str = Field(default = "New product")
    tags: List[str] = Field(default = ["Tag1", "Tag2", "Tag3"])
    amount: int = Field(default = 0)
    available: Optional[bool] = Field()
    status: Optional[int] = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()

class ProductDataSimple(BaseModel):
    id: int 
    name: str = Field(default = "Example_product")
    branch: str = Field(default = "saga")
    description: str = Field(default = "New product")
    tags: List[str] = Field(default = ["Tag1", "Tag2", "Tag3"])
    amount: int = Field(default = 0)


