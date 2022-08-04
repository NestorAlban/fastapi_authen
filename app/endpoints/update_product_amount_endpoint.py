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

from app.usercase import ProductAmountUpdate
from app.schemas import UpdateProductAmount, ProductDataSimple


router = APIRouter()

UPDATE_PRODUCT_AMOUNT_ERROR_MESSAGE: Final = "ERROR IN update_product_amount ENDPOINT"
UPDATE_PRODUCT_AMOUNT_ENDPOINT_SUMMARY: Final = "Update a Product amount"
UPDATE_PRODUCT_AMOUNT_ENDPOINT_PATH: Final = "/product/{id}/update_amount"
SUCCESS_KEY: Final = "success"
PRODUCT_KEY: Final = "user"


@router.put(
    path=UPDATE_PRODUCT_AMOUNT_ENDPOINT_PATH,
    status_code=status.HTTP_200_OK,
    response_model=Dict[str, Any],
    summary=UPDATE_PRODUCT_AMOUNT_ENDPOINT_SUMMARY,
    tags=["Products"],
)
def update_product_amount(product_info: UpdateProductAmount):
    success = False
    products_response = None
    try:
        product_update = ProductAmountUpdate()
        amount = product_info.amount

        if type(amount) == int:
            products = product_update.run(UpdateProductAmount(
                id=product_info.id, 
                amount = amount
            ))
            if products:
                success = True
                products_response = ProductDataSimple(**products.__dict__)
    except Exception as error:
        logging.error(UPDATE_PRODUCT_AMOUNT_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, PRODUCT_KEY: products_response}
