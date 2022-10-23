from app.services import ProductService
from pydantic import Field, BaseModel
from app.database.database import UserDomain
from app.schemas import ProductInfoBack



class ProductCreator:
    def __init__(self):
        ProductInfoBack
        pass

    def run(self, params: ProductInfoBack):
        product_service = ProductService()
        product = product_service.create_product(
            params.name,
            params.branch,
            params.description,
            params.tags
        )
        return product