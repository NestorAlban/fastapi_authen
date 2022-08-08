from app.database import DataBase

from typing import List


class CompanyService:
    def __init__(self):
        self.alchemy_db = DataBase()
        pass

    def create_company(
        self, 
        name: str, 
    ):
        company = self.alchemy_db.create_company(
            name,
        )
        print("==============success2============")
        return company