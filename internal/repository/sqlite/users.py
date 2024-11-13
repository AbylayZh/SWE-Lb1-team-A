import bcrypt
from sqlalchemy.orm import Session

from internal.repository.models.users import User, Farmer, Buyer, Admin


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def Create(self, first_name, last_name, email, phone, password) -> int:
        try:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            new_user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone,
                password=hashed_password
            )

            self.db.add(new_user)
            # self.db.commit()
            # self.db.refresh(new_user)
            self.db.flush()

            return new_user.id
        except Exception as e:
            self.db.rollback()
            raise e

    def ReadByEmail(self, email: str) -> User:
        try:
            return self.db.query(User).filter(User.email == email).first()
        except Exception as e:
            self.db.rollback()
            raise e

    def ReadByID(self, id: int) -> User:
        try:
            return self.db.query(User).filter(User.id == id).first()
        except Exception as e:
            self.db.rollback()
            raise e


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


class BuyerRepository:
    def __init__(self, db: Session):
        self.db = db

    def Create(self, user_id, address, payment):
        try:
            new_buyer = Buyer(
                user_id=user_id,
                delivery_address=address,
                preferred_payment=payment
            )

            self.db.add(new_buyer)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
