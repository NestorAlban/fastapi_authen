from app.services import ProductService
from app.models import Product
from pydantic import Field
from app.schemas import ProductId

class ProductIdGetter:
    def __init__(self):
        pass

    def run(self, params: ProductId) -> Product:
        product_service = ProductService()
        product = product_service.get_product_id(params.id)
        return product
    