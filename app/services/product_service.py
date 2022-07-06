from app.models import Product
from app.database import ProductDomaint
from app.database import DataBase

from typing import List


class ProductService:
    def __init__(self):
        self.alchemy_db = DataBase()
        pass

    def create_product(
        self, 
        name: str, 
        branch: str,
        description: str,
        tags: List[str]
    ):
        product = self.alchemy_db.create_product(
            name, 
            branch,
            description,
            tags
        )
        print("==============success2============")
        return product

    def get_all_products(self):
        products = []
        products = self.alchemy_db.get_all_products()
        return products

    def get_product_name(
        self, 
        part_name: str
    ):
        products = []
        products = self.alchemy_db.get_product_name(part_name)
        print("============================2")
        print(products, type(products))
        return products

    def get_product_tag(
        self, 
        part_tags: str
    ):
        products = []
        products = self.alchemy_db.get_product_tag(part_tags)
        print("============================2")
        print(products, type(products))
        return products