from app.models import Sells
from app.database import SellsDomaint
from app.database import DataBase

from typing import List


class SellService:
    def __init__(self):
        self.alchemy_db = DataBase()
        pass

    def create_sell(
        self, 
        user: int, 
        product: int, 
    ):
        sell = self.alchemy_db.create_sell(
            user, 
            product,
        )
        print("==============success2============")
        return sell
        