from sqlalchemy.orm import Session

from internal.repository.models.farms import Farm


class FarmRepository:
    def __init__(self, db: Session):
        self.db = db

    def Create(self, farmer_id: int, farm_size: int, farm_address: str):
        try:
            new_farm = Farm(
                farmer_id=farmer_id,
                farm_size=farm_size,
                farm_address=farm_address
            )
            self.db.add(new_farm)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def get_farm_by_id(self, farm_id: int) -> Farm:
        """Fetches a farm by its ID."""
        try:
            return self.db.query(Farm).filter(Farm.id == farm_id).first()
        except Exception as e:
            self.db.rollback()
            raise e

    def update_farm(self, farm_id: int, farm_size: float = None, farm_address: str = None) -> bool:
        """Updates the specified fields of a farm entry by ID."""
        try:
            farm = self.get_farm_by_id(farm_id)
            if not farm:
                return False  # Farm with given ID does not exist
            if farm_size is not None:
                farm.farm_size = farm_size
            if farm_address is not None:
                farm.farm_address = farm_address
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise e

    def delete_farm(self, farm_id: int) -> bool:
        """Deletes a farm by its ID."""
        try:
            farm = self.get_farm_by_id(farm_id)
            if not farm:
                return False  # Farm with given ID does not exist
            self.db.delete(farm)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise e

    def list_all_farms(self) -> list:
        """Retrieves all farm entries."""
        try:
            return self.db.query(Farm).all()
        except Exception as e:
            self.db.rollback()
            raise e
