from app.services import ProductService
from typing import List
from app.models import Product


class AllProductGetter:
    def __init__(self):
        pass

    def run(self) -> List[Product]:
        products = []
        product_service = ProductService()
        products = product_service.get_all_products()
        return products