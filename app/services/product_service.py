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
        print("=PRODUCT PARAMS=")
        print(name)
        print(branch)
        print(description)
        print(tags)
        product = self.alchemy_db.create_product(
            name, 
            branch,
            description,
            tags
        )
        print("==============asdasdasd2============")
        print(product)
        return product

    def delete_product_id(
        self, 
        id: int
    ):
        product = self.alchemy_db.delete_product_id(id)
        return product

    def get_all_products(self):
        products = []
        products = self.alchemy_db.get_all_products()
        return products

    def get_product_id(
        self, 
        id: int
    ):
        products = []
        products = self.alchemy_db.get_product_id(id)
        return products

    def get_product_name(
        self, 
        part_name: str
    ):
        products = []
        products = self.alchemy_db.get_product_name(part_name)
        return products

    def get_product_tag(
        self, 
        part_tags: str
    ):
        products = []
        products = self.alchemy_db.get_product_tag(part_tags)
        return products

    def get_product_branch(
        self, 
        part_branch: str
    ):
        products = []
        products = self.alchemy_db.get_product_branch(part_branch)
        return products

    def update_product_info(
        self, 
        id: int, 
        name: str, 
        branch: str,
        description: str
    ):
        products = self.alchemy_db.update_product_info(
            id, 
            name, 
            branch,
            description
        )
        return products

    def update_product_amount(
        self, 
        id: int,
        amount: int,
    ):
        products = self.alchemy_db.update_product_amount(
            id, 
            amount
        )
        return products