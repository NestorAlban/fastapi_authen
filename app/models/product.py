from typing import List
from sqlalchemy import (
    Column, 
    ForeignKey, 
    String, 
    Integer, 
    DateTime, 
    Boolean,
    func,
    PickleType, 
    Table
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship, backref



Base = declarative_base()

class Product(Base):
    __tablename__ = "product"

    id = Column(
        Integer, 
        primary_key = True
    )
    name = Column(
        String, 
        nullable = False, 
        unique = True
    )
    branch = Column(
        String, 
        nullable = False, 
        unique = False
    )
    description = Column(
        String, 
        nullable = False, 
        unique = False
    )
    amount = Column(
        Integer(), 
        default = 0, 
        nullable = False
    )
    tags = Column(
        MutableList.as_mutable(PickleType), 
        default = [], 
        nullable = False
    )
    available = Column(
        Boolean(), 
        default = False, 
        nullable = False
    )
    status = Column(
        Integer(), 
        default = 0, 
        nullable = False
    )
    created_at = Column(
        DateTime, 
        default = func.now(), 
        nullable = False
    )
    updated_at = Column(
        DateTime, 
        default = func.now(), 
        nullable = False, 
        onupdate = func.now()
    )

