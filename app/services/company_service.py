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
        return company

    def delete_company_id(
        self, 
        id: int
    ):
        company = self.alchemy_db.delete_company_id(id)
        return company

    def get_company_name(
        self, 
        part_name: str
    ):
        companies = []
        companies = self.alchemy_db.get_company_name(part_name)
        return companies