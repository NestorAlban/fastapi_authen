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

from app.usercase import ProductTagGetter
from app.schemas import ProductTag, ProductData


router = APIRouter()

GET_PRODUCT_TAG_ERROR_MESSAGE: Final = "ERROR IN product tag ENDPOINT"
PRODUCT_TAG_ENDPOINT_SUMMARY: Final = "Show Products per tags"
PRODUCT_TAG_ENDPOINT_PATH: Final = "/Product/{tag}"
PRODUCT_KEY: Final = "product"

@router.get(
    path=PRODUCT_TAG_ENDPOINT_PATH,
    response_model=Dict[str, Any],
    status_code=status.HTTP_200_OK,
    summary=PRODUCT_TAG_ENDPOINT_SUMMARY,
    tags=["Products"],
)
def get_product_tag(tag: str = Path(
    ..., 
    title="Tag1"
    )
):
    product_tag_response = []
    tag_lower = tag.lower()
    try:
        product_tag_getter = ProductTagGetter()
        product_tag = product_tag_getter.run(ProductTag(tags = tag_lower))
        print("============================4")
        print(product_tag, type(product_tag))
        if product_tag:
            product_tag_response = [
                ProductData(**product.__dict__) for product in product_tag
            ]
    except Exception as error:
        logging.error(GET_PRODUCT_TAG_ERROR_MESSAGE, error)
    return {PRODUCT_KEY: product_tag_response}
