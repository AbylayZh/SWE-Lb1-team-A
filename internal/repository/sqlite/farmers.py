from sqlalchemy.orm import Session

from internal.repository.models.users import Farmer


class FarmerRepository:
    def __init__(self, db: Session):
        self.db = db

    def Create(self, user_id):
        try:
            new_farmer = Farmer(
                user_id=user_id,
            )

            self.db.add(new_farmer)
            # self.db.commit()
            self.db.flush()

            return new_farmer.id
        except Exception as e:
            self.db.rollback()
            raise e
