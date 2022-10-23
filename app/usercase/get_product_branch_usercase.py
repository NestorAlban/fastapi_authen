from app.services import ProductService
from app.models import Product
from pydantic import Field
from app.schemas import ProductBranch

class ProductBranchGetter:
    def __init__(self):
        pass

    def run(self, params: ProductBranch) -> Product:
        product_service = ProductService()
        product = product_service.get_product_branch(params.branch)
        return product