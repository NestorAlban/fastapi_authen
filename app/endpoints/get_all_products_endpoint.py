import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import List
from typing import Optional
from typing import Final
from datetime import datetime
from app.usercase import AllProductGetter
from app.schemas import ProductData

router = APIRouter()

GET_ALL_PRODUCTS_ERROR_MESSAGE: Final = "ERROR IN get all products ENDPOINT"
ALL_PRODUCTS_ENDPOINT_SUMMARY: Final = "Show all Products"
ALL_PRODUCTS_ENDPOINT_PATH: Final = "/all_products"


@router.get(
    path=ALL_PRODUCTS_ENDPOINT_PATH,
    response_model=List[ProductData],
    status_code=status.HTTP_200_OK,
    summary=ALL_PRODUCTS_ENDPOINT_SUMMARY,
    tags=["Products"],
)
def get_all_products():
    all_products_response = []
    try:
        all_products_getter = AllProductGetter()
        products = all_products_getter.run()
        all_products_response = [ProductData(**product.__dict__) for product in products]
    except Exception as error:
        logging.error(GET_ALL_PRODUCTS_ERROR_MESSAGE, error)
    return all_products_response