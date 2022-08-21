import pytest
from app.usercase import AllProductGetter
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
FIRST_PRODUCT = {
    'name': EXAMPLE_NAME, 
    'branch': EXAMPLE_BRANCH, 
    'description': EXAMPLE_DESCRIPTION, 
    'tags': EXAMPLE_TAGS
}
SECOND_PRODUCT = {
    'name': EXAMPLE_NAME+'1', 
    'branch': EXAMPLE_BRANCH, 
    'description': EXAMPLE_DESCRIPTION+'1', 
    'tags': EXAMPLE_TAGS
}
def test_get_product(app, create_products, delete_products):
    db = DataBase()
    ids_to_erase = []
    company_service = CompanyService()
    product_service = ProductService()
    company_created = company_service.create_company(EXAMPLE_BRANCH)
    print('=============================after company created===============================')
    print('\n\n\n',company_created, company_created.id)
    product_created = create_products(
        [FIRST_PRODUCT,
        SECOND_PRODUCT,]
    )
    print('=============================after prducts created===============================')
    print(
        product_created, 
        '\n', 
        company_created
    )
    for prod in product_created:
        prod_id = prod.id
        print(prod_id)
        ids_to_erase.append(prod_id)
    print (ids_to_erase)
    client = TestClient(app)
    response = client.get(
        "/all_products",
        json={
            
        }
    ).json()
    print('==============response===================')
    print(response) 

    assert response 
    assert response[0].get('name')== EXAMPLE_NAME
    assert response[1].get('name')== EXAMPLE_NAME+'1'
    delete_products(ids_to_erase)
    company_service.delete_company_id(company_created.id)
