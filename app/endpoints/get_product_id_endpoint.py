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

from app.usercase import ProductIdGetter
from app.schemas import ProductId, ProductData


router = APIRouter()

GET_PRODUCT_ID_ERROR_MESSAGE: Final = "ERROR IN product id ENDPOINT"
PRODUCT_ID_ENDPOINT_SUMMARY: Final = "Show Products per ids"
PRODUCT_ID_ENDPOINT_PATH: Final = "/product/id/{id}"
PRODUCT_KEY: Final = "product"

@router.get(
    path=PRODUCT_ID_ENDPOINT_PATH,
    response_model=Dict[str, Any],
    status_code=status.HTTP_200_OK,
    summary=PRODUCT_ID_ENDPOINT_SUMMARY,
    tags=["Products"],
)
def get_product_name(id: int = Path(
    ..., 
    title="Product ID"
    )
):
    product_response = []
    try:
        product_id_getter = ProductIdGetter()
        product_id = product_id_getter.run(ProductId(id = id))
        if product_id:
            # product_response = ProductData(**product_id.__dict__)
            product_response = ProductData.construct(
                id = product_id.id,
                name = product_id.name,
                branch = product_id.branch,
                description = product_id.description,
                tags = product_id.tags,
                amount = product_id.amount,
                available = product_id.available,
                status = product_id.status,
                created_at = product_id.created_at,
                updated_at = product_id.updated_at,
            ).dict(by_alias=True)
    except Exception as error:
        logging.error(GET_PRODUCT_ID_ERROR_MESSAGE, error)
    return {PRODUCT_KEY: product_response}
