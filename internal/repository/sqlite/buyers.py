from sqlalchemy.orm import Session

from internal.repository.models.users import Buyer


class BuyerRepository:
    def __init__(self, db: Session):
        self.db = db

    def Create(self, user_id, address, payment):
        try:
            new_buyer = Buyer(
                user_id=user_id,
                delivery_address=address,
                preferred_payment_id=payment
            )

            self.db.add(new_buyer)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
