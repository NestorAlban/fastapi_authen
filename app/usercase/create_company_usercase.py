from app.services import CompanyService
from pydantic import Field, BaseModel
from app.database.database import UserDomain
from app.schemas import CompanyName



class CompanyCreator:
    def __init__(self):
        pass

    def run(self, params: CompanyName):
        company_service = CompanyService()
        company = company_service.create_company(
            params.name,
        )
        return company