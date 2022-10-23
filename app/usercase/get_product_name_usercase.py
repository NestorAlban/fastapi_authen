from app.services import ProductService
from app.models import Product
from pydantic import Field
from app.schemas import ProductName

class ProductNameGetter:
    def __init__(self):
        pass

    def run(self, params: ProductName) -> Product:
        product_service = ProductService()
        product = product_service.get_product_name(params.name)
        return product

