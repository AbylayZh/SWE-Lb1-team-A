from sqlalchemy.orm import Session

from internal.repository.sqlite.users import BuyerRepository
from internal.validators.users import BuyerSignupRequest


class BuyerService:
    def __init__(self, db: Session):
        self.buyer_repository = BuyerRepository(db)

    def Register(self, user_id, req: BuyerSignupRequest):
        try:
            self.buyer_repository.Create(user_id, req.delivery_address, req.preferred_payment)
        except Exception as e:
            raise e
