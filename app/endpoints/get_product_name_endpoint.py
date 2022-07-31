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

from app.usercase import ProductNameGetter
from app.schemas import ProductName, ProductData


router = APIRouter()

GET_PRODUCT_NAME_ERROR_MESSAGE: Final = "ERROR IN product name ENDPOINT"
PRODUCT_NAME_ENDPOINT_SUMMARY: Final = "Show Products per names"
PRODUCT_NAME_ENDPOINT_PATH: Final = "/product/na/{name}"
PRODUCT_KEY: Final = "product"

@router.get(
    path=PRODUCT_NAME_ENDPOINT_PATH,
    response_model=Dict[str, Any],
    status_code=status.HTTP_200_OK,
    summary=PRODUCT_NAME_ENDPOINT_SUMMARY,
    tags=["Products"],
)
def get_product_name(name: str = Path(
    ..., 
    title="Example_product"
    )
):
    product_name_response = []
    name_lower = name.lower()
    try:
        product_name_getter = ProductNameGetter()
        product_name = product_name_getter.run(ProductName(name = name_lower))
        print("============================4")
        print(product_name, type(product_name))
        if product_name:
            product_name_response = [
                ProductData(**product.__dict__) for product in product_name
            ]
    except Exception as error:
        logging.error(GET_PRODUCT_NAME_ERROR_MESSAGE, error)
    return {PRODUCT_KEY: product_name_response}
