from app.services import ProductService
from typing import List
from app.models import User
from pydantic import Field
from pydantic import BaseModel
from app.schemas import UpdateProductInfo


class ProductInfoUpdate:
    def __init__(self):
        pass

    def run(self, params: UpdateProductInfo):
        product_service = ProductService()
        products = product_service.update_product_info(
            params.id, 
            params.name, 
            params.branch,
            params.description
        )
        return products