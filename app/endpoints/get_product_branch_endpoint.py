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

from app.usercase import ProductBranchGetter
from app.schemas import ProductBranch, ProductData


router = APIRouter()

GET_PRODUCT_BRANCH_ERROR_MESSAGE: Final = "ERROR IN product branch ENDPOINT"
PRODUCT_BRANCH_ENDPOINT_SUMMARY: Final = "Show Products per branch"
PRODUCT_BRANCH_ENDPOINT_PATH: Final = "/product/ba/{branch}"
PRODUCT_KEY: Final = "product"

@router.get(
    path=PRODUCT_BRANCH_ENDPOINT_PATH,
    response_model=Dict[str, Any],
    status_code=status.HTTP_200_OK,
    summary=PRODUCT_BRANCH_ENDPOINT_SUMMARY,
    tags=["Products"],
)
def get_product_branch(
    branch: str = Path(
    ..., 
    title="Example_branch"
    )
):
    product_branch_response = []
    branch_lower = branch.lower()
    try:
        product_branch_getter = ProductBranchGetter()
        product_branch = product_branch_getter.run(ProductBranch(branch = branch_lower))
        if product_branch:
            product_branch_response = [
                ProductData(**product.__dict__) for product in product_branch
            ]
    except Exception as error:
        logging.error(GET_PRODUCT_BRANCH_ERROR_MESSAGE, error)
    return {PRODUCT_KEY: product_branch_response}
