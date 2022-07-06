from app.services import ProductService
from app.models import Product
from pydantic import Field
from app.schemas import ProductTag

class ProductTagGetter:
    def __init__(self):
        pass

    def run(self, params: ProductTag) -> Product:
        product_service = ProductService()
        product = product_service.get_product_tag(params.tags)
        print("============================3")
        print(product, type(product))
        return product
