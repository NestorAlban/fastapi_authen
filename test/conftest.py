import sys
from typing import List
from app.services.company_service import CompanyService
from app.services.product_service import ProductService
from app.services import UserService
import pytest
from venv import create
from dotenv import load_dotenv
from app.endpoints.app import create_app
from app.database import DataBase

load_dotenv()
EXAMPLE_NAME = "Example Name"
EXAMPLE_BRANCH = "Example Branch"
EXAMPLE_DESCRIPTION = "Example Description"
EXAMPLE_TAGS = ["Example Tag", "Example Tag", "Example Tag"]
sys.path.append("app/")
_db = DataBase()

@pytest.fixture(scope="session")
def app():
    _app = create_app()
    _app.testing = True

    return _app

@pytest.fixture(scope="function")
def create_user():
    def _create_user(name, email, password):
        user_service = UserService()
        user_created = user_service.create_user(
            name,
            email,
            password,
        )
        return user_created
    return _create_user

@pytest.fixture(scope="function")
def create_product():
    def _create_product(name, branch, description, tags):
        product_service = ProductService()
        product_created = product_service.create_product(
                name,
                branch,
                description,
                tags
        )

        return product_created
    return _create_product

@pytest.fixture(scope="function")
def delete_companies():
    def _delete_companies(branches: List[str]):
        company_service = CompanyService()
        companies_got = []
        for branch in branches:
            company_got = company_service.delete_company_id(
                branch.get('id'),
            )
            companies_got.append(company_got)

        return companies_got
    return _delete_companies

@pytest.fixture(scope="function")
def create_products():
    def _create_products(products: List[str]):
        product_service = ProductService()
        products_created = []
        for product in products:
            product_created = product_service.create_product(
                product.get("name"),
                product.get("branch"),
                product.get("description"),
                product.get("tags"),
            )
            products_created.append(product_created)
        return products_created
    return _create_products

@pytest.fixture(scope="function")
def delete_products():
    def _delete_products(products: List[str]):
        product_service = ProductService()
        products_deleted = []
        for product in products:
            product_deleted = product_service.delete_product_id(
                product,
            )
            products_deleted.append(product_deleted)
        return products_deleted
    return _delete_products

# @pytest.fixture(scope="session")
# def db(app):
#     """
#     Returns session-wide initialised database.
#     """
#     # with app.app_context():
#     database = "postgres://postgres:postgres@127.0.0.1:5438/sellsdb"
#     # for database in databases:
#     _db.session.drop_all(database)
#     _db.session.create_all(database)

#     yield _db
#     _db.session.drop_all(database)


# @pytest.fixture(scope="function", autouse=True)
# def session(app, db):
#     """
#     Returns function-scoped session.
#     """
#     with app.app_context():

#         # establish  a SAVEPOINT just before beginning the test
#         # (http://docs.sqlalchemy.org/en/latest/orm/session_transaction.html#using-savepoint)
#         db 
#         _db.begin_nested()

#         @event.listens_for(_db.session, "after_transaction_end")
#         def restart_savepoint(sess2, trans):
#             # Detecting whether this is indeed the nested transaction of the test
#             if trans.nested and not trans._parent.nested:
#                 # The test should have normally called session.commit(),
#                 # but to be safe we explicitly expire the session
#                 sess2.expire_all()
#                 _db.begin_nested()

#         yield _db

#         # Cleanup
#         _db.remove()
#         # This instruction rolls back any commit that were executed in the tests.
#         _db.rollback()