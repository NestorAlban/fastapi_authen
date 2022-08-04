from sqlalchemy import (
    Column, 
    ForeignKey, 
    String, 
    Integer, 
    DateTime, 
    Boolean,
    func, 
    Table
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from .import User, Product


Base = declarative_base()

class Sells(Base):
    __tablename__ = "sell"

    id = Column(
        Integer, 
        primary_key = True
    )
    user = Column(
        Integer,
        ForeignKey(User.id),
        nullable = False,
    )
    product = Column(
        Integer,
        ForeignKey(Product.id),
        nullable = False, 
    )
    status = Column(
        Integer(), 
        default = 0, 
        nullable = False
    )
    payment = Column(
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
    user1 = relationship(
        User,
        back_populates = 'sell'
    )
    product1 = relationship(
        Product,
        back_populates = 'sell'
    )
