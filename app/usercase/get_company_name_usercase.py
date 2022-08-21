from app.services import CompanyService
from app.models import Branch
from pydantic import Field
from app.schemas import CompanyName

class CompanyNameGetter:
    def __init__(self):
        pass

    def run(self, params: CompanyName) -> Branch:
        company_service = CompanyService()
        company = company_service.get_company_name(params.name)
        print("============================3")
        print(company, type(company))
        return company