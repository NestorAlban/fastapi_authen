from app.services import EnrollmentService
from pydantic import Field, BaseModel

from app.schemas import EnrollmentInfoBack



class EnrollmentCreator:
    def __init__(self):
        pass

    def run(self, params: EnrollmentInfoBack):
        enrollment_service = EnrollmentService()
        enrollment = enrollment_service.create_enrollment(
            params.user,
            params.vendor,
        )
        return enrollment