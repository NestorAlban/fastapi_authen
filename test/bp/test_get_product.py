import pytest
from app.usercase import ProductIdGetter
from app.schemas import ProductId
from app.database import DataBase
from app.models import User
from app.database import DataBase
from app.services import ProductService, CompanyService, product_service
EXAMPLE_NAME = "Example Name"
EXAMPLE_BRANCH = "Example Branch"
EXAMPLE_DESCRIPTION = "Example Description"
EXAMPLE_TAGS = ["Example Tag", "Example Tag", "Example Tag"]
EXAMPLE_COMP_NAME = "Example Company Name"
def test_get_product(create_product):
    db = DataBase()
    company_service = CompanyService()
    product_service = ProductService()
    company_created = company_service.create_company(EXAMPLE_BRANCH)
    print('=============================after company created===============================')
    print('\n\n\n',company_created, company_created.id)
    product_created = create_product(
        name=EXAMPLE_NAME,
        branch=EXAMPLE_BRANCH,
        description=EXAMPLE_DESCRIPTION,
        tags=EXAMPLE_TAGS,
    )
    print(
        product_created, 
        '\n', 
        company_created
    )
    # company_getter = company_service.get_company_name(EXAMPLE_BRANCH.lower())
    # print('=============================after company getter===============================')
    # print('\n\n\n', company_getter)
    product_getter = ProductIdGetter()
    product = product_getter.run(ProductId(
        id = product_created.id,
    ))
    # user = db.session.query(User).filter(User.id==user_created.id).first()

    print('============================')
    print(
        product,
        '\n', 
    )

    assert product is not None
    assert product.name == EXAMPLE_NAME
    product_service.delete_product_id(product.id)
    company_service.delete_company_id(company_created.id)