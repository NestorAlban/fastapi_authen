import logging
from pydantic import BaseModel
from pydantic import Field
from fastapi import status
from fastapi import APIRouter
from typing import Final
from typing import Optional
from datetime import datetime

from app.usercase import EnrollmentCreator
from app.schemas import (
    EnrollmentData, 
    EnrollmentInfoBack,
)

router = APIRouter()

CREATE_ENROLLMENT_ERROR_MESSAGE: Final = "ERROR IN create_enrollment ENDPOINT"
CREATE_ENROLLMENT_ENDPOINT_SUMMARY: Final = "Create a new Enrollment"
CREATE_ENROLLMENT_ENDPOINT_PATH: Final = "/create_enrollment"
SUCCESS_KEY: Final = "success"
ENROLLMENT_KEY: Final = "enrollment"



@router.post(
    path=CREATE_ENROLLMENT_ENDPOINT_PATH,
    status_code=status.HTTP_201_CREATED,
    summary=CREATE_ENROLLMENT_ENDPOINT_SUMMARY,
    tags=["Enrollment"],
)
def create_enrollment(new_enrollment_data: EnrollmentInfoBack):
    success = False
    enrollment_response = None
    enrollment = None
    try:
        enrollment_creator = EnrollmentCreator()
        user_q = new_enrollment_data.user
        vendor_q = new_enrollment_data.vendor

        enrollment = enrollment_creator.run(EnrollmentInfoBack(
            user = user_q, 
            vendor = vendor_q,
            )
        )
        if enrollment:
            enrollment_response = EnrollmentData.construct(
                id = enrollment.id,
                user = enrollment.user,
                vendor = enrollment.vendor,
                created_at = enrollment.created_at,
                updated_at = enrollment.updated_at,
            ).dict(by_alias=True)
            success = True
    except Exception as error:
        logging.error(CREATE_ENROLLMENT_ERROR_MESSAGE, error)
    return {SUCCESS_KEY: success, ENROLLMENT_KEY: enrollment_response}

