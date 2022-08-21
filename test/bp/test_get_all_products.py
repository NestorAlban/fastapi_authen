import pytest
from app.usercase import AllProductGetter
from app.schemas import ProductId
from app.database import DataBase
from app.models import User
from app.database import DataBase
from app.services import ProductService, CompanyService, product_service
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
def test_get_product(create_products, delete_products):
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
    all_products_getter = AllProductGetter()
    products = all_products_getter.run()
    print('============================')
    print(
        products,
        '\n', 
    )

    assert products is not None
    assert products[0].name == EXAMPLE_NAME
    assert products[1].name == EXAMPLE_NAME+'1'
    # product_service.delete_product_id(product.id)
    delete_products(ids_to_erase)
    company_service.delete_company_id(company_created.id)