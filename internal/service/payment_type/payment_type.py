from typing import List

from sqlalchemy.orm import Session

from internal.repository.models.payment_types import PaymentType
from internal.repository.sqlite.payment_types import PaymentTypeRepository


class PaymentTypeService:
    def __init__(self, db: Session):
        self.payment_type_repository = PaymentTypeRepository(db)

    def GetAll(self) -> List[PaymentType]:
        try:
            return self.payment_type_repository.ReadAll()
        except Exception as e:
            raise e
