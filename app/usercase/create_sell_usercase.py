from app.services import SellService
from pydantic import Field, BaseModel
from app.database.database import UserDomain
from app.schemas import SellInfoBack



class SellCreator:
    def __init__(self):
        SellInfoBack
        pass

    def run(self, params: SellInfoBack):
        sell_service = SellService()
        sell = sell_service.create_sell(
            params.user,
            params.product,
        )
        print("==============success1============")
        return sell