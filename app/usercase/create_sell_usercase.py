from app.services import (
    SellService, 
    UserService, 
    ProductService
)
from pydantic import Field, BaseModel
from app.database.database import UserDomain
from app.schemas import SellInfoBack



class SellCreator:
    def __init__(self):
        SellInfoBack
        pass

    def run(self, params: SellInfoBack):
        sell = None
        sell_service = SellService()
        user_service = UserService()
        product_service = ProductService()
        is_user_valid = user_service.get_user_id(params.user)
        is_product_valid = product_service.get_product_id(params.product)
        if is_product_valid and is_user_valid:
            sell = sell_service.create_sell(
                params.user,
                params.product,
            )
        print("==============success1============")
        return {
            'sell':sell,
            'user': is_user_valid,
            'product': is_product_valid,
        }