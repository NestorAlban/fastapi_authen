import logging
from fastapi import (
    Body,
    HTTPException, 
    Path, 
    Depends,
)
import fastapi
from fastapi.security import (
    OAuth2PasswordBearer, 
    OAuth2PasswordRequestForm
)

import os
import uuid
from requests import Session
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import true as sa_true
from sqlalchemy.exc import IntegrityError

from app.models import (
    User, 
    Product,
    Branch,
    Sells
)

from typing import Final
from typing import List
from datetime import datetime
from typing import Optional

import psycopg2
from psycopg2 import Error
from psycopg2.extras import RealDictCursor
from psycopg2.errors import UniqueViolation

from passlib.context import CryptContext

from ..models.user import Enrollment, Vendor
from .hash_pass import Hash_Password
from .token import Token
from .oauth import GetCurrentUsers
from .domain import (
    UserDomaint,
    ProductDomaint, 
    Domain
)
from .mail import Mail

from app.schemas import UserData

from dataclasses import dataclass

logger = logging.getLogger(__name__)
logger.level = logger.setLevel(logging.INFO)
DATABASE_CONNECTION_ERROR: Final = "Error while connecting to PostgreSQL"
CLOSED_DATABASE_MESSAGE: Final = "PostgreSQL connection is closed"
CONNECTING_DB_MESSAGE: Final = "Connecting PostgreSQL database======"
DELETED_USER: Final = False
ACTIVE_USER: Final = True
ACTIVE_PRODUCT: Final = True
DEACTIVATE_PRODUCT: Final = False
CANNOT_PROCEED_MESSAGE: Final = "Cannot proceed: "
SPACES_FOR_MESSAGE: Final = "============================"

@dataclass(frozen=True)
class UserDomain:
    id: int
    name: str
    email: str
    password: str
    is_active: Optional[bool]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


# pwd_cxt = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

class DataBase:
    def __init__(self) -> None:
        self.database_user = os.getenv("DATABASE_USER")
        self.database_password = os.getenv("DATABASE_PASSWORD")
        self.database_host = os.getenv("DATABASE_HOST")
        self.database_port = os.getenv("DATABASE_PORT")
        self.database_name = os.getenv("DATABASE_NAME")
        self.engine = create_engine(
            f"postgresql://{self.database_user}:{self.database_password}@{self.database_host}:{self.database_port}/{self.database_name}",
            echo=True,
            future=True,
        )
        Session = sessionmaker(self.engine)
        self.session = Session()

    #Login

    @staticmethod
    def login_user_domain(user):
        user_domain = UserDomain(
            user.name, 
            user.email,
            user.password,
            user.is_active, 
            user.created_at, 
            user.updated_at
        )
        return user_domain

    def login_user(
        self, 
        name: str, 
        password: str
    ):
        user = None
        token_value = None
        token_type = None
        user = self.session.query(
            User
        ).filter(
            User.name == name
        ).first()
        if user:
            user_domain= Domain.create_user_domain(user)
            print("============================")
            print(user_domain.password)
            print(password)
            print(Hash_Password.bcrypt(password))
            print("============================")
            
            if Hash_Password.verify_pass(
                user_domain.password,
                password
            ):
                access_token = Token.create_access_token(
                    data={"sub": user_domain.name}
                )
                token_value = access_token
                token_type = "bearer"
            else:
                raise HTTPException(
                    status_code = fastapi.status.HTTP_404_NOT_FOUND,
                    detail = f"Incorrect password"
                )
        
        self.session.close()
        return {"user": user, "token": (token_value, token_type)}


    ##Users

    @staticmethod
    def create_user_domain(user):
        #you can use the UserDomain in this file or UserDomaint in domain.py file in this folder
        user_domain = UserDomaint(
            user.id, 
            user.name, 
            user.email, 
            user.password,
            user.is_active, 
            user.created_at,
            user.updated_at
        )
        return user_domain


    def create_user(
        self, 
        name: str, 
        email: str, 
        password: str
    ):
        user_domain = None
        user = User(
            name = name, 
            email = email, 
            password = Hash_Password.bcrypt(password)
        )
        try:
            if user:
                self.session.add(user)
                self.session.commit()
                # can user the create_user_domain in this file or in domain file
                # user_domain = DataBase.create_user_domain(user)

                user_domain = Domain.create_user_domain(user)
                print("============================")
                print(user_domain.id)
                print("============================")
        except IntegrityError as e:
            assert isinstance(e.orig, UniqueViolation)
        self.session.close()
        return user_domain

    def delete_user_id(
        self, 
        id: int, 
    ):
        user_domain = None
        user = None
        try:
            user = self.session.query(
                User
            ).filter(
                User.id == id
            ).first()
            if user:
                self.session.delete(user)
                self.session.commit()
                user_domain = Domain.create_user_domain(user)
        except IntegrityError as e:
            assert isinstance(e.orig, UniqueViolation)
        self.session.close()
        return user_domain


    def get_user_id(
        self, 
        id: int, 
        get_current_user: UserData = Depends(GetCurrentUsers.get_current_user)
    ):
        user_domain = None
        user = None
        user = self.session.query(
            User
        ).filter(
            User.id == id
        ).first()
        if user: 
            user_domain = Domain.create_user_domain(user)
        self.session.close()
        return user

    def get_all_users(self):
        users = self.session.query(User).all()
        for user in users:
            print(user)
            if user:
                user_domain = Domain.create_user_domain(user)
                print("=====================get_all_users1=======================")
                print(user_domain, type(user_domain), user_domain.id)
                print("=====================get_all_users1=======================")
        self.session.close()
        # user_response=[UserDomain(**user.__dict__) for user in users]
        # print(user_response)
        return users

    def get_all_active_users(self):
        users = self.session.query(
            User
        ).filter(
            User.is_active == sa_true()
        ).all()
        self.session.close()
        return users

    def change_user_password(
        self, 
        email: str
    ):
        user = None
        code = None
        print("Email>error data 1")
        user = self.session.query(
            User
        ).filter(
            User.email == email
        ).first()
        print(user)
        print("Email>error data 2")
        if user:
            code = str(uuid.uuid1())
            user_domain=Domain.create_user_domain(user)
            print(user_domain, type(user_domain), user_domain.id)
        self.session.close()

        #Sending Mail

        subject = "Password"
        recipient = [user_domain.email]
        message = """
        <!DOCTYPE html>
        <html>
        <body>
        <div style="width:100%;font-family: monospace;">
            <h1>Hello, {0:}</h1>
            <p>Your reset code is {1:}</p>
        </div>
        </body>
        </html>
        """.format(user_domain.email, code)
        print("Email>error data 3")
        # print(Mail)
        # send = Mail.send_email(subject, recipient, message)
        
        # print(send)
        return {"user": user, "reset_code": code}

    def update_user(
        self, 
        id: int, 
        name: str, 
        email: str
    ):
        user_domain = None
        user = self.session.query(User).filter(User.id == id).first()
        if user:
            user.name = name
            user.email = email
            self.session.commit()
            user_domain = Domain.create_user_domain(user)
        self.session.close()
        return user_domain

    def deactivate_user(
        self, 
        id: int
    ):
        user_domain = None
        user = self.session.query(User).filter(User.id == id).first()
        if user:
            user.is_active = DELETED_USER
            self.session.commit()
            user_domain = Domain.create_user_domain(user)
        self.session.close()
        return user_domain

    def activate_user(
        self, 
        id: int
    ):
        user_domain = None
        user = self.session.query(User).filter(User.id == id).first()
        if user:
            user.is_active = ACTIVE_USER
            self.session.commit()
            user_domain = Domain.create_user_domain(user)
        self.session.close()
        return user_domain

    def update_user_role(
        self, 
        id: int, 
        role: int
    ):
        user_domain = None
        user = None
        vendor = None
        vendor_domain = None
        user = self.session.query(User).filter(User.id == id).first()
        vendor = self.session.query(Vendor).filter(Vendor.name == id).first()
        if user:
            user.role = role
            self.session.commit()
            
            user_domain = Domain.create_user_domain(user)
            if role == 1:
                if not vendor:
                    vendor = Vendor(
                        name = user_domain.id
                    )
                    self.session.add(vendor)
                if vendor and vendor.status != role:
                    vendor.status = role
                self.session.commit()
                print("=====================vendor created==================")
            elif role == 0:
                # vendor = self.session.query(Vendor).filter(Vendor.name == id).first()
                if vendor.status != role:
                    vendor.status = role
                    self.session.commit()
                print("=====================vendor deactivated==================")
            vendor_domain = Domain.create_vendor_domain(vendor)
            print(vendor_domain.id)
            print(f'================vendor status = {vendor_domain.status}==============')
        self.session.close()
        return user_domain

    def update_user_status(
        self, 
        id: int, 
        status: int
    ):
        user_domain = None
        user = self.session.query(
            User
        ).filter(
            User.id == id
        ).first()
        if user:
            user.status = status
            self.session.commit()
            user_domain = Domain.create_user_domain(user)
        self.session.close()
        return user_domain

    ##Vendor 

    def create_vendor(self):
        pass

    ##Enrollment

    def create_enrollment(
        self,
        user_id: int, 
        vendor_id: int, 
    ):
        user_q = None
        user_domain = None
        user_domain_vendor = None
        vendor_q = None
        vendor_domain = None
        enrollment_domain = None
        enrollment = None
        validate_user_id = None
        validate_vendor_id = None
        validate_vendor_status = None
        user_q = self.session.query(
            User
        ).filter(
            User.id == user_id
        ).first()
        vendor_q = self.session.query(
            Vendor
        ).filter(
            Vendor.id == vendor_id
        ).first()
        
        if user_q and vendor_q:
            user_domain = Domain.create_user_domain(user_q)
            vendor_domain = Domain.create_vendor_domain(vendor_q)
            validate_user_id = user_domain.id
            validate_vendor_id = vendor_domain.name
            validate_vendor_status = vendor_domain.status
            print(f'user id {validate_user_id}, vendor id {validate_vendor_id}')
            vendor_name_q = self.session.query(
                User
            ).filter(
                User.id == validate_vendor_id
            ).first()
            user_domain_vendor = Domain.create_user_domain(vendor_name_q)
            user_name = user_domain.name
            vendor_name = user_domain_vendor.name
            try:
                if validate_user_id != validate_vendor_id:
                    if validate_vendor_status != 0:
                        enrollment = Enrollment(
                            user = user_id,
                            vendor = vendor_id
                        )
                        if enrollment:
                            self.session.add(enrollment)
                            self.session.commit()
                            enrollment_domain = Domain.create_enrollment_domain(enrollment)
                        print(SPACES_FOR_MESSAGE)
                        print(
                            enrollment_domain.id, 
                            enrollment_domain.user, 
                            enrollment_domain.vendor
                        )
                        print(
                            SPACES_FOR_MESSAGE +
                            f'user name {user_name}, vendor name {vendor_name}' +
                            SPACES_FOR_MESSAGE
                        )
                        print(SPACES_FOR_MESSAGE)
                    else:
                        print(
                            SPACES_FOR_MESSAGE +
                            CANNOT_PROCEED_MESSAGE + 
                            "the vendor is not active" +
                            SPACES_FOR_MESSAGE
                        )
                else:
                    print(
                        SPACES_FOR_MESSAGE +
                        CANNOT_PROCEED_MESSAGE + 
                        "the user cannot buy to itself" +
                        SPACES_FOR_MESSAGE
                    )
            except IntegrityError as e:
                assert isinstance(e.orig, UniqueViolation)
        self.session.close()
        return enrollment_domain

    ##Products

    def create_product(
        self, 
        name: str, 
        branch: str,
        description: str,
        tags: str
    ):
        product_domain = None
        company_domain = None
        company = None
        branch_lower = branch.lower()
        try:
            company = self.session.query(
                Branch
            ).filter(
                func.lower(Branch.name).contains(branch_lower)
            ).all()
            
            if company:
                for comp in company:
                    company_domain = Domain.create_company_domain(comp)
                    print(
                        company_domain.id,
                        company_domain.name
                    )
                    if branch_lower == company_domain.name.lower():
                        product = Product(
                            name = name, 
                            branch = company_domain.name,
                            description = description,
                            tags = tags
                        )
                        if product:
                            self.session.add(product)
                            self.session.commit()
                            # can product the create_product_domain in this file or in domain file
                            # product_domain = DataBase.create_product_domain(product)
                            product_domain = Domain.create_product_domain(product)
                            print("============================")
                            print(product_domain.id)
                            print("============================")
        except IntegrityError as e:
            print(e)
            assert isinstance(e.orig, UniqueViolation)
        self.session.close()
        return product_domain

    def delete_product_id(
        self, 
        id: int, 
    ):
        product_domain = None
        product = None
        try:
            product = self.session.query(
                Product
            ).filter(
                Product.id == id
            ).first()
            if product:
                self.session.delete(product)
                self.session.commit()
                product_domain = Domain.create_product_domain(product)
        except IntegrityError as e:
            assert isinstance(e.orig, UniqueViolation)
        self.session.close()
        return product_domain

    def get_all_products(self):
        products = self.session.query(Product).all()
        for product in products:
            print(product)
            if product:
                product_domain = Domain.create_product_domain(product)
                print("=====================get_all_products1=======================")
                print(product_domain, type(product_domain), product_domain.id)
                print("=====================get_all_products1=======================")
        self.session.close()
        return products

    def get_product_id(
        self, 
        id: int, 
    ):
        product_domain = None
        product = None
        product = self.session.query(
            Product
        ).filter(
            Product.id == id
        ).first()
        print("id============================1")
        if product:
            product_domain = Domain.create_product_domain(product)
        self.session.close()
        return product_domain
    
    def get_product_name(
        self, 
        part_name: str
    ):
        product = None
        product = self.session.query(
            Product
        ).filter(
            func.lower(Product.name).contains(part_name)
        )
        print("============================1")
        print(product, type(product))
        self.session.close()
        return product

    def get_product_tag(
        self, 
        part_tags: str
    ):
        #explicar al sql
        product = None
        print("============4-a=================")
        product = self.session.query(
            Product
        ).filter(
            Product.tags.contains([part_tags])
        ).all()
        print("============4-b=================")
        print(product, type(product))
        for prod in product:
            if prod:
                print("============4-c=================")
                product_domain = Domain.create_product_domain(prod)
                print("=====================get_tag_products1=======================")
                print(product_domain, type(product_domain), product_domain.id)
                print("=====================get_tag_products1=======================")
        self.session.close()
        return product

    def get_product_branch(
        self, 
        part_branch: str
    ):
        product = None
        product_domain = None
        product = self.session.query(
            Product
        ).filter(
            func.lower(Product.branch).contains(part_branch)
        )
        print("branch============================1")
        print(product, type(product))
        for prod in product:
            print(prod)
            if prod:
                product_domain = Domain.create_product_domain(prod)
                print(product_domain, type(product_domain),  
                product_domain.tags, 
                type(product_domain.tags), product_domain.tags[0],
                product_domain.tags[0].lower())

        self.session.close()
        return product

    def update_product_info(
        self, 
        id: int, 
        name: str, 
        branch: str,
        description: str
    ):
        product_domain = None
        product = self.session.query(Product).filter(Product.id == id).first()
        if product:
            product.name = name
            product.branch = branch
            product.description = description
            self.session.commit()
            product_domain = Domain.create_product_domain(product)
        self.session.close()
        return product_domain

    def update_product_amount(
        self, 
        id: int, 
        amount: int, 
    ):
        product_domain = None
        product = self.session.query(Product).filter(Product.id == id).first()
        if product:
            product.amount = amount
            if amount == 0:
                product.available = DEACTIVATE_PRODUCT
            else:
                product.available = ACTIVE_PRODUCT
            self.session.commit()
            product_domain = Domain.create_product_domain(product)
        self.session.close()
        return product_domain

    ##Company

    def create_company(
        self, 
        name: str, 
    ):
        company_domain = None
        company = Branch(
            name = name, 
        )
        try:
            if company:
                self.session.add(company)
                self.session.commit()

                company_domain = Domain.create_company_domain(company)
                print("============================")
                print(company_domain.id)
                print("============================")
        except IntegrityError as e:
            assert isinstance(e.orig, UniqueViolation)
        self.session.close()
        return company_domain

    ##Sells

    def create_sell(
        self, 
        user: int, 
        product: int, 
    ):
        sell_domain = None
        user_cap = None
        product_cap = None
        
        sell = Sells(
            user = user, 
            product = product,
        )
        try:
            
            if sell:
                product_cap = self.session.query(
                    Product
                ).filter(
                    Product.id == product
                ).first()
                user_cap = self.session.query(
                    User
                ).filter(
                    User.id == user
                ).first()
                if product_cap and user_cap:
                    self.session.add(sell)
                    self.session.commit()
                    sell_domain = Domain.create_sell_domain(sell)
                    print("============================")
                    print(sell_domain.id)
                    print("============================")
        except IntegrityError as e:
            assert isinstance(e.orig, UniqueViolation)
        self.session.close()
        return sell