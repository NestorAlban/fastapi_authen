import pytest
from app.usercase import ProductIdGetter
from app.schemas import ProductId
from app.database import DataBase
from app.models import User
from app.database import DataBase
from app.services import ProductService, CompanyService, product_service
from fastapi.testclient import TestClient
EXAMPLE_NAME = "Example Name"
EXAMPLE_BRANCH = "Example Branch"
EXAMPLE_DESCRIPTION = "Example Description"
EXAMPLE_TAGS = ["Example Tag", "Example Tag", "Example Tag"]
def test_get_product(app, create_product):
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
    client = TestClient(app)
    response = client.get(
        "/product/id/{}".format(product_created.id),
        json={
            "id": product_created.id,
        }
    ).json()
    print('==============response===================')
    print(response) 
    product = response.get('product')
    # user = response.get('user')
    assert response 
    assert product.get('name') == EXAMPLE_NAME
    product_service.delete_product_id(product_created.id)
    company_service.delete_company_id(company_created.id)

    