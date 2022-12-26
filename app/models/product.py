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
    Table,
    ARRAY
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship, backref
from sqlalchemy.dialects.postgresql import ARRAY



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
        ForeignKey('company.name'),
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
        # MutableList.as_mutable(PickleType), 
        ARRAY(String()),
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
    company = relationship(
        'Branch',
        back_populates = 'product'
    )
    # tags = relationship(
    #     'Tags',
    #     back_populates = 'product'
    # )

class Branch(Base):
    __tablename__ = "company"

    id = Column(
        Integer, 
        primary_key = True
    )
    name = Column(
        String, 
        nullable = False, 
        unique = True
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
    product = relationship(
        'Product',
        back_populates = 'company'
    )

# class Tags(Base):
#     __tablename__ = "tags"

#     id = Column(
#         Integer, 
#         primary_key = True
#     )
#     name = Column(
#         String, 
#         nullable = False, 
#         unique = True
#     )
#     status = Column(
#         Integer(), 
#         default = 1, 
#         nullable = False
#     )
#     created_at = Column(
#         DateTime, 
#         default = func.now(), 
#         nullable = False
#     )
#     updated_at = Column(
#         DateTime, 
#         default = func.now(), 
#         nullable = False, 
#         onupdate = func.now()
#     )
#     product = relationship(
#         'Product',
#         back_populates = 'tags'
#     )