from sqlalchemy.orm import Session

from internal.repository.models.payment_types import PaymentType


class PaymentTypeRepository:
    def __init__(self, session: Session):
        self.db = session

    def ReadAll(self):
        try:
            return self.db.query(PaymentType).all()
        except Exception as e:
            self.db.rollback()
            raise e
