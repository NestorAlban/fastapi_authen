from app.models import User
from app.database import UserDomain
from app.database import DataBase

from typing import List


class EnrollmentService:
    def __init__(self):
        self.alchemy_db = DataBase()
        pass

    def create_enrollment(
        self, 
        user_id: int, 
        vendor_id: int, 
    ) -> UserDomain:
        enrollment = None
        enrollment = self.alchemy_db.create_enrollment(
            user_id,
            vendor_id
        )
        return enrollment