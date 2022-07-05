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
    ):
        product = self.alchemy_db.create_product(
            name, 
            branch
        )
        print("==============success2============")
        return product