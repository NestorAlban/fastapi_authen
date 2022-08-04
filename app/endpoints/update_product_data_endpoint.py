import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import Any
from typing import Final
from typing import Dict
from typing import Optional
from datetime import datetime

from app.usercase import ProductInfoUpdate
from app.schemas import UpdateProductInfo, ProductDataSimple


router = APIRouter()

UPDATE_PRODUCT_INFO_ERROR_MESSAGE: Final = "ERROR IN update_product_info ENDPOINT"
UPDATE_PRODUCT_INFO_ENDPOINT_SUMMARY: Final = "Update a new Product"
UPDATE_PRODUCT_INFO_ENDPOINT_PATH: Final = "/product/{id}/update_info"
SUCCESS_KEY: Final = "success"
PRODUCT_KEY: Final = "user"


@router.put(
    path=UPDATE_PRODUCT_INFO_ENDPOINT_PATH,
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, Any],
    summary=UPDATE_PRODUCT_INFO_ENDPOINT_SUMMARY,
    tags=["Products"],
)
def update_product_info(product_info: UpdateProductInfo):
    success = False
    products_response = None
    try:
        product_update = ProductInfoUpdate()
        name = product_info.name.strip()
        branch= product_info.branch.strip()
        description = product_info.description.strip()

        if len(name) != 0 and len(branch) != 0 and len(description) != 0:
            products = product_update.run(UpdateProductInfo(
                id=product_info.id, 
                name=name, 
                branch = branch,
                description = description
            ))
            if products:
                success = True
                products_response = ProductDataSimple(**products.__dict__)
    except Exception as error:
        logging.error(UPDATE_PRODUCT_INFO_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, PRODUCT_KEY: products_response}
