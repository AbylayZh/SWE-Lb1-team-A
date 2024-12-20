from sqlalchemy.orm import Session

from internal.repository.models.errors import NotFoundError
from internal.repository.models.users import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def Create(self, first_name, last_name, email, phone, password) -> int:
        try:
            new_user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone,
                password=password
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
            user = self.db.query(User).filter(User.email == email).first()
            if user:
                return user
            else:
                raise NotFoundError()
        except Exception as e:
            self.db.rollback()
            raise e

    def ReadByID(self, id: int) -> User:
        try:
            user = self.db.query(User).filter(User.id == id).first()
            if user:
                return user
            else:
                raise NotFoundError()
        except Exception as e:
            self.db.rollback()
            raise e

    def Delete(self, user_id: int):
        try:
            user = self.ReadByID(user_id)
            self.db.delete(user)  # Mark the user for deletion
            self.db.commit()  # Commit to apply the deletion
        except Exception as e:
            self.db.rollback()
            raise e

    def UpdatePassword(self, user_id: int, new_password: str):
        try:
            user = self.ReadByID(user_id)
            user.password = new_password  # Update the password field
            self.db.commit()  # Commit the change to the database
        except Exception as e:
            self.db.rollback()
            raise e

    def UpdateApproved(self, user_id: int, new_approved: int):
        try:
            user = self.ReadByID(user_id)
            user.approved = new_approved  # Update the password field
            self.db.commit()  # Commit the change to the database
        except Exception as e:
            self.db.rollback()
            raise e

    def UpdateActive(self, user_id: int, new_active: int):
        try:
            user = self.ReadByID(user_id)
            user.active = new_active  # Update the password field
            self.db.commit()  # Commit the change to the database
        except Exception as e:
            self.db.rollback()
            raise e

    def ReadUnapprovedAll(self):
        try:
            return self.db.query(User).filter(User.approved == 0).all()
        except Exception as e:
            self.db.rollback()
            raise e

    def ReadActiveAll(self):
        try:
            return self.db.query(User).filter(User.active == 1).all()
        except Exception as e:
            self.db.rollback()
            raise e

    def ReadInactiveAll(self):
        try:
            return self.db.query(User).filter(User.active == 0).all()
        except Exception as e:
            self.db.rollback()
            raise e
