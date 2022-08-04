from app.services import ProductService
from typing import List
from app.models import User
from pydantic import Field
from pydantic import BaseModel
from app.schemas import UpdateProductAmount


class ProductAmountUpdate:
    def __init__(self):
        pass

    def run(self, params: UpdateProductAmount):
        product_service = ProductService()
        products = product_service.update_product_amount(
            params.id, 
            params.amount, 
        )
        return products