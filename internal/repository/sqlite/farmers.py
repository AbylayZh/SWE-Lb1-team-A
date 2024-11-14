import bcrypt
from sqlalchemy.orm import Session

from internal.repository.models.users import User, Farmer, Buyer, Admin


class FarmerRepository:
    def __init__(self, db: Session):
        self.db = db

    def Create(self, user_id):
        try:
            new_farmer = Farmer(
                user_id=user_id,
            )

            self.db.add(new_farmer)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
