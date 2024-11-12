from sqlalchemy.orm import Session
from internal.repository.models.errors import SQLDefaultError, SQLConstraintError
from internal.repository.models.farm_repository import FarmRepository
from internal.repository.models.farm import Farm


class FarmService:
    def __init__(self, db: Session):
        # Initialize FarmRepository with the session
        self.farm_repo = FarmRepository(db)

    def create_farm(self, farm_size: float, farmer_id: int, farm_address: str) -> int:
        """Creates a new farm and returns its ID."""
        try:
            return self.farm_repo.create_farm(farm_size, farmer_id, farm_address)
        except (SQLDefaultError, SQLConstraintError) as e:
            print(f"Error creating farm: {e}")
            raise

    def get_farm(self, farm_id: int) -> Farm:
        """Fetches a farm by its ID."""
        farm = self.farm_repo.get_farm_by_id(farm_id)
        if farm is None:
            raise ValueError(f"Farm with ID {farm_id} not found.")
        return farm

    def update_farm(self, farm_id: int, farm_size: float = None, farm_address: str = None) -> bool:
        """Updates the specified fields of a farm entry by ID."""
        try:
            updated = self.farm_repo.update_farm(farm_id, farm_size, farm_address)
            if not updated:
                raise ValueError(f"Farm with ID {farm_id} not found.")
            return updated
        except (SQLDefaultError, SQLConstraintError) as e:
            print(f"Error updating farm: {e}")
            raise

    def delete_farm(self, farm_id: int) -> bool:
        """Deletes a farm by its ID."""
        try:
            deleted = self.farm_repo.delete_farm(farm_id)
            if not deleted:
                raise ValueError(f"Farm with ID {farm_id} not found.")
            return deleted
        except SQLDefaultError as e:
            print(f"Error deleting farm: {e}")
            raise

    def list_farms(self) -> list:
        """Retrieves all farms."""
        try:
            return self.farm_repo.list_all_farms()
        except SQLDefaultError as e:
            print(f"Error listing farms: {e}")
            raise