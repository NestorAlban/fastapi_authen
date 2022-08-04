from typing import List, Optional
from datetime import datetime

from dataclasses import dataclass

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

    