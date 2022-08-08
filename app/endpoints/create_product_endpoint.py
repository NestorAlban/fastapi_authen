import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import Final
from typing import Optional
from datetime import datetime

from app.usercase import ProductCreator
from app.schemas import UserData, UserInfoBack, ProductInfoBack, ProductData
from app.database import Mapping_rath

router = APIRouter()

CREATE_PRODUCT_ERROR_MESSAGE: Final = "ERROR IN create_product ENDPOINT"
CREATE_PRODUCT_ENDPOINT_SUMMARY: Final = "Create a new Product"
CREATE_PRODUCT_ENDPOINT_PATH: Final = "/create_product"
SUCCESS_KEY: Final = "success"
PRODUCT_KEY: Final = "product"


@router.post(
    path=CREATE_PRODUCT_ENDPOINT_PATH,
    status_code=status.HTTP_201_CREATED,
    summary=CREATE_PRODUCT_ENDPOINT_SUMMARY,
    tags=["Products"],
)
def create_product(new_product_data: ProductInfoBack):
    success = False
    product_response = None
    try:
        product_creator = ProductCreator()
        name = new_product_data.name.strip()
        branch = new_product_data.branch.strip()
        description = new_product_data.description.strip()
        tags = new_product_data.tags

        if len(name) != 0 and len(branch) != 0 and len(description) !=0:
            product = product_creator.run(ProductInfoBack(
                name = name, 
                branch = branch.lower(),
                description = description,
                tags = tags
                )
            )
            if product:
                product_response = ProductData.construct(
                    id = product.id,
                    name = product.name,
                    branch = product.branch,
                    description = product.description,
                    tags = product.tags,
                    amount = product.amount,
                    available = product.available,
                    status = product.status,
                    created_at = product.created_at,
                    updated_at = product.updated_at,
                ).dict(by_alias=True)
                success = True
                print("==============success============")
    except Exception as error:
        logging.error(CREATE_PRODUCT_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, PRODUCT_KEY: product_response}