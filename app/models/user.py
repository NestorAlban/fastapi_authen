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
from sqlalchemy.orm import relationship, backref


Base = declarative_base()

class User(Base):
    __tablename__ = "user_password"

    id = Column(
        Integer, 
        primary_key = True
    )
    name = Column(
        String, 
        nullable = False, 
        unique = True
    )
    email = Column(
        String, 
        nullable = False, 
        unique = True
    )
    password = Column(
        String, 
        nullable = False, 
        unique = True
    )
    is_active = Column(
        Boolean(), 
        default = True, 
        nullable = False
    )
    status = Column(
        Integer(), 
        default = 1, 
        nullable = False
    )
    role = Column(
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
    vendor = relationship(
        'Vendor',
        secondary = enrollment_table,
        back_populates = 'user_password'
    )

class Vendor(Base):
    __tablename__ = "vendor"

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
        default = 1, 
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
    user = relationship(
        'User',
        secondary = enrollment_table,
        back_populates = 'vendor',
        # secondary = 'Enrollment',
    )

# class Enrollment(Base):
#     __tablename__ = "enrollment"

#     id = Column(
#         Integer, 
#         primary_key = True
#     )
#     user = Column(
#         Integer, 
#         ForeignKey("user_password.id"),
#         nullable = False,
#     )
#     vendor = Column(
#         Integer(), 
#         ForeignKey("vendor.id"),
#         nullable = False,
#     )

enrollment_table = Table(
    "enrollment",
    Base.metadata,
    Column(
        'id',
        Integer, 
        primary_key = True
    ),
    Column(
        'user',
        Integer, 
        ForeignKey("user_password.id"),
        nullable = False,
    ),
    Column(
        'vendor',
        Integer, 
        ForeignKey("vendor.id"),
        nullable = False,
    )
)