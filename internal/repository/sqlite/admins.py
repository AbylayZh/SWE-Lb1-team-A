import bcrypt
from sqlalchemy.orm import Session

from internal.repository.models.users import User, Farmer, Buyer, Admin


class AdminRepository:
    def __init__(self, db: Session):
        self.db = db

    def Create(self, user_id):
        try:
            new_admin = Admin(
                user_id=user_id,
            )

            self.db.add(new_admin)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
