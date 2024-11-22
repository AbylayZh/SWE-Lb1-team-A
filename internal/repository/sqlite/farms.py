from sqlalchemy.orm import Session

from internal.repository.models.farms import Farm


class FarmRepository:
    def __init__(self, db: Session):
        self.db = db

    def Create(self, farmer_id: int, farm_size: int, farm_address: str):
        try:
            new_farm = Farm(
                farmer_id=farmer_id,
                size=farm_size,
                address=farm_address
            )
            self.db.add(new_farm)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
