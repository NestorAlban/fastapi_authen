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
    # vendor = relationship(
    #     'Vendor',
    #     back_populates = 'user_password'
    # )
    vendor = relationship(
        'Vendor',
        # back_populates = 'user_password',
    )
    enrollment = relationship(
        'Enrollment',
        # back_populates = 'user_password',
    )

class Vendor(Base):
    __tablename__ = "vendor"

    id = Column(
        Integer, 
        primary_key = True
    )
    # name = Column(
    #     String, 
    #     nullable = False, 
    #     unique = True
    # )
    name = Column(
        Integer, 
        ForeignKey("user_password.id"),
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
    # user = relationship(
    #     'User',
    #     back_populates = 'vendor',
    #     # secondary = enrollment_table,
    #     # secondary = 'Enrollment',
    # )
    user = relationship(
        'User',
        back_populates = 'vendor',
    )
    enrollment = relationship(
        'Enrollment',
        # back_populates = 'vendor',
    )

class Enrollment(Base):
    __tablename__ = "enrollment"

    id = Column(
        Integer, 
        primary_key = True
    )
    user = Column(
        Integer, 
        ForeignKey("user_password.id"),
        nullable = False,
    )
    vendor = Column(
        Integer(), 
        ForeignKey("vendor.id"),
        nullable = False,
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
    vendor_relation = relationship(
        'Vendor',
        back_populates = 'enrollment'
    )
    user_relation = relationship(
        'User',
        back_populates = 'enrollment'
    )


# enrollment_table = Table(
#     "enrollment",
#     Base.metadata,
#     Column(
#         'id',
#         Integer, 
#         primary_key = True
#     ),
#     Column(
#         'user',
#         Integer, 
#         ForeignKey("user_password.id"),
#         nullable = False,
#     ),
#     Column(
#         'vendor',
#         Integer, 
#         ForeignKey("vendor.id"),
#         nullable = False,
#     )
# )