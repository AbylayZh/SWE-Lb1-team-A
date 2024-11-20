from sqlalchemy.orm import Session

from internal.repository.sqlite.farmers import FarmerRepository
from internal.validators.users import FarmerSignupRequest


class FarmerService:
    def __init__(self, db: Session):
        self.farmer_repository = FarmerRepository(db)

    def Register(self, user_id, req: FarmerSignupRequest):
        try:
            return self.farmer_repository.Create(user_id)
        except Exception as e:
            raise e
