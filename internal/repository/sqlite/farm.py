from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import Session
from internal.repository.models.errors import SQLDefaultError, SQLConstraintError
from internal.repository.models.farm import Farm

class FarmRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_farm(self, farm_size: float, farmer_id: int, farm_address: str) -> int:
        """Creates a new farm entry."""
        try:
            new_farm = Farm(
                farm_size=farm_size,
                farmer_id=farmer_id,
                farm_address=farm_address
            )
            self.db.add(new_farm)
            self.db.flush()  # Flush to access new_farm.id before commit
            return new_farm.id
        except IntegrityError as e:
            self.db.rollback()
            raise SQLConstraintError(e)
        except SQLAlchemyError as e:
            self.db.rollback()
            raise SQLDefaultError(e)

    def get_farm_by_id(self, farm_id: int) -> Farm:
        """Fetches a farm by its ID."""
        try:
            return self.db.query(Farm).filter(Farm.id == farm_id).first()
        except SQLAlchemyError as e:
            raise SQLDefaultError(e)

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
        except IntegrityError as e:
            self.db.rollback()
            raise SQLConstraintError(e)
        except SQLAlchemyError as e:
            self.db.rollback()
            raise SQLDefaultError(e)

    def delete_farm(self, farm_id: int) -> bool:
        """Deletes a farm by its ID."""
        try:
            farm = self.get_farm_by_id(farm_id)
            if not farm:
                return False  # Farm with given ID does not exist
            self.db.delete(farm)
            self.db.commit()
            return True
        except SQLAlchemyError as e:
            self.db.rollback()
            raise SQLDefaultError(e)

    def list_all_farms(self) -> list:
        """Retrieves all farm entries."""
        try:
            return self.db.query(Farm).all()
        except SQLAlchemyError as e:
            raise SQLDefaultError(e)
