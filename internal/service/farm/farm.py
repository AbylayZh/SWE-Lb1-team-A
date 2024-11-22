from sqlalchemy.orm import Session

from internal.repository.models.farms import Farm
from internal.repository.sqlite.farms import FarmRepository
from internal.validators.users import FarmerSignupRequest


class FarmService:
    def __init__(self, db: Session):
        # Initialize FarmRepository with the session
        self.farm_repository = FarmRepository(db)

    def Register(self, farmer_id: int, req: FarmerSignupRequest) -> int:
        farm_size, farm_address = req.farm_size, req.farm_address

        try:
            self.farm_repository.Create(farmer_id, farm_size, farm_address.title())
        except Exception as e:
            raise e

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
        except Exception as e:
            raise e

    def delete_farm(self, farm_id: int) -> bool:
        """Deletes a farm by its ID."""
        try:
            deleted = self.farm_repo.delete_farm(farm_id)
            if not deleted:
                raise ValueError(f"Farm with ID {farm_id} not found.")
            return deleted
        except Exception as e:
            raise e

    def list_farms(self) -> list:
        """Retrieves all farms."""
        try:
            return self.farm_repo.list_all_farms()
        except Exception as e:
            raise e
