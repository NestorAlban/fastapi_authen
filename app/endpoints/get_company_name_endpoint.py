import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import Path, Depends
from fastapi import status
from fastapi import APIRouter
from typing import Dict
from typing import Optional
from typing import Final
from typing import Any

from datetime import datetime

from app.usercase import CompanyNameGetter
from app.schemas import CompanyName, CompanyData


router = APIRouter()

GET_COMPANY_NAME_ERROR_MESSAGE: Final = "ERROR IN company name ENDPOINT"
COMPANY_NAME_ENDPOINT_SUMMARY: Final = "Show Company per names"
COMPANY_NAME_ENDPOINT_PATH: Final = "/company/na/{name}"
COMPANY_KEY: Final = "company"

@router.get(
    path=COMPANY_NAME_ENDPOINT_PATH,
    response_model=Dict[str, Any],
    status_code=status.HTTP_200_OK,
    summary=COMPANY_NAME_ENDPOINT_SUMMARY,
    tags=["Companies"],
)
def get_company_name(name: str = Path(
    ..., 
    title="Example_company"
    )
):
    company_name_response = []
    name_lower = name.lower()
    try:
        company_name_getter = CompanyNameGetter()
        company = company_name_getter.run(CompanyName(name = name_lower))
        if company:
            company_name_response = [
                CompanyData(**comp.__dict__) for comp in company
            ]
    except Exception as error:
        logging.error(GET_COMPANY_NAME_ERROR_MESSAGE, error)
    return {COMPANY_KEY: company_name_response}
