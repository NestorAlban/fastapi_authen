import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import Final
from typing import Optional
from datetime import datetime

from app.usercase import SellCreator
from app.schemas import (
    SellInfoBack, 
    SellData, 
    SellFullData
)
from app.database import Mapping_rath

router = APIRouter()

CREATE_SELL_ERROR_MESSAGE: Final = "ERROR IN create_sell ENDPOINT"
CREATE_SELL_ENDPOINT_SUMMARY: Final = "Create a new Sell"
CREATE_SELL_ENDPOINT_PATH: Final = "/create_sell"
SUCCESS_KEY: Final = "success"
SELL_KEY: Final = "product"


@router.post(
    path=CREATE_SELL_ENDPOINT_PATH,
    status_code=status.HTTP_201_CREATED,
    summary=CREATE_SELL_ENDPOINT_SUMMARY,
    tags=["Sells"],
)
def create_sell(new_sell_data: SellInfoBack):
    success = False
    sell_response = None
    sell_response_1 = None
    try:
        sell_sell_response = None
        sell_user_response = None
        sell_product_response = None
        sell_creator = SellCreator()
        user = new_sell_data.user
        product = new_sell_data.product

        if user != 0 and product != 0 and type(user) == int and type(product) == int:
            sell = sell_creator.run(SellInfoBack(
                user = user, 
                product = product
                )
            )
            print(sell)
            sell_sell_response = sell.get('sell')
            sell_user_response = sell.get('user')
            sell_product_response = sell.get('product')
            if sell_sell_response:
                sell_response = SellData.construct(
                    id = sell_sell_response.id,
                    user = sell_sell_response.user,
                    product = sell_sell_response.product,
                    status = sell_sell_response.status,
                    payment = sell_sell_response.payment,
                    created_at = sell_sell_response.created_at,
                    updated_at = sell_sell_response.updated_at,
                ).dict(by_alias=True)
                sell_response_1 = SellFullData.construct(
                    id = sell_sell_response.id,
                    user = sell_user_response.name,
                    email = sell_user_response.email,
                    product = sell_sell_response.product,
                    status = sell_sell_response.status,
                    payment = sell_sell_response.payment,
                    created_at = sell_sell_response.created_at,
                    updated_at = sell_sell_response.updated_at,
                ).dict(by_alias=True)
                success = True
                print("==============success============")
    except Exception as error:
        logging.error(CREATE_SELL_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, SELL_KEY: sell_response}