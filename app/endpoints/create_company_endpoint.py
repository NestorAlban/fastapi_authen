import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import Final
from typing import Optional
from datetime import datetime

from app.usercase import CompanyCreator
from app.schemas import CompanyName, CompanyData
from app.database import Mapping_rath

router = APIRouter()

CREATE_COMPANY_ERROR_MESSAGE: Final = "ERROR IN create_company ENDPOINT"
CREATE_COMPANY_ENDPOINT_SUMMARY: Final = "Create a new Company"
CREATE_COMPANY_ENDPOINT_PATH: Final = "/create_company"
SUCCESS_KEY: Final = "success"
COMPANY_KEY: Final = "company"


@router.post(
    path=CREATE_COMPANY_ENDPOINT_PATH,
    status_code=status.HTTP_201_CREATED,
    summary=CREATE_COMPANY_ENDPOINT_SUMMARY,
    tags=["Company"],
)
def create_product(new_company_data: CompanyName):
    success = False
    company_response = None
    try:
        company_creator = CompanyCreator()
        name = new_company_data.name.strip()

        if len(name) != 0:
            company = company_creator.run(CompanyName(
                name = name,
                ))
            if company:
                company_response = CompanyData.construct(
                    id = company.id,
                    name = company.name,
                    status = company.status,
                    created_at = company.created_at,
                    updated_at = company.updated_at,
                ).dict(by_alias=True)
                success = True
                print("==============success============")
    except Exception as error:
        logging.error(CREATE_COMPANY_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, COMPANY_KEY: company_response}