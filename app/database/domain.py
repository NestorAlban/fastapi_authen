from typing import List, Optional
from datetime import datetime

from dataclasses import dataclass

##User

@dataclass(frozen=True)
class UserDomaint:
    id: int
    name: str
    email: str
    password: str
    is_active: Optional[bool]
    status: int 
    role: int 
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

@dataclass(frozen=True)
class VendorDomaint:
    id: int
    name: Optional[int]
    status: int 
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

@dataclass(frozen=True)
class EnrollmentDomaint:
    id: int
    user: Optional[int]
    vendor: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

##Product

@dataclass(frozen=True)
class ProductDomaint:
    id: int
    name: str
    branch: str
    description: str
    tags: List[str]
    amount: int
    available: Optional[bool]
    status: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

@dataclass(frozen=True)
class CompanyDomaint:
    id: int
    name: str
    status: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

##Sells

@dataclass(frozen=True)
class SellsDomaint:
    id: int
    user: int
    product: int
    status: int 
    payment: int 
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class Domain:
    def __init__(self) -> None:
        pass

    @staticmethod
    def create_user_domain(user):
        #you can use the UserDomain in this file or UserDomaint in domain.py file in this folder
        user_domain = UserDomaint(
            user.id, 
            user.name, 
            user.email, 
            user.password,
            user.is_active, 
            user.status,
            user.role,
            user.created_at,
            user.updated_at
        )
        return user_domain

    @staticmethod
    def create_vendor_domain(vendor):
        vendor_domain = VendorDomaint(
            vendor.id, 
            vendor.name, 
            vendor.status,
            vendor.created_at,
            vendor.updated_at
        )
        return vendor_domain

    @staticmethod
    def create_enrollment_domain(enrollment):
        enrollment_domain = EnrollmentDomaint(
            enrollment.id, 
            enrollment.user,
            enrollment.vendor,
            enrollment.created_at,
            enrollment.updated_at
        )
        return enrollment_domain

    @staticmethod
    def create_product_domain(product):
        #you can use the ProductDomain in this file or ProductDomaint in domain.py file in this folder
        product_domain = ProductDomaint(
            product.id,
            product.name,
            product.branch,
            product.description,
            product.tags,
            product.amount,
            product.available,
            product.status,
            product.created_at,
            product.updated_at
        )
        return product_domain

    @staticmethod
    def create_company_domain(company):
        company_domain = CompanyDomaint(
            company.id,
            company.name,
            company.status,
            company.created_at,
            company.updated_at
        )
        return company_domain

    @staticmethod
    def create_sell_domain(sells):
        sells_domain = SellsDomaint(
            sells.id,
            sells.user,
            sells.product,
            sells.status,
            sells.payment,
            sells.created_at,
            sells.updated_at
        )
        return sells_domain

    