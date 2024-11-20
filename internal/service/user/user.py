import bcrypt
from sqlalchemy.orm import Session

from internal.repository.models.errors import InvalidCredentialsError
from internal.repository.models.users import User
from internal.repository.sqlite.users import UserRepository
from internal.validators.users import LoginRequest, SignupRequest


class UserService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def Authenticate(self, req: LoginRequest) -> int:
        email, password = req.email, req.password

        try:
            user = self.user_repository.ReadByEmail(email)
            if not user:
                raise InvalidCredentialsError()

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                raise InvalidCredentialsError()

            return user.id
        except Exception as e:
            raise e

    def Register(self, req: SignupRequest) -> int:
        first_name, last_name, email, phone, password = req.first_name, req.last_name, req.email, req.phone, req.password

        try:
            return self.user_repository.Create(first_name.capitalize(), last_name.capitalize(), email.lower(), phone,
                                               password)
        except Exception as e:
            raise e

    def Get(self, user_id) -> User:
        try:
            return self.user_repository.ReadByID(user_id)
        except Exception as e:
            raise e

    def Delete(self, user_id):
        try:
            self.user_repository.Delete(user_id)
        except Exception as e:
            raise e

    def UpdatePassword(self, user_id: int, password: str) -> int:
        try:
            return self.user_repository.UpdatePassword(user_id, password)
        except Exception as e:
            raise e

    def Approve(self, user_id: int):
        try:
            self.user_repository.UpdateApproved(user_id, 1)
        except Exception as e:
            raise e

    def Enable(self, user_id: int):
        try:
            self.user_repository.UpdateActive(user_id, 1)
        except Exception as e:
            raise e

    def Disable(self, user_id: int):
        try:
            self.user_repository.UpdateActive(user_id, 0)
        except Exception as e:
            raise e

    def GetUnapprovedAll(self):
        try:
            return self.user_repository.ReadUnapprovedAll()
        except Exception as e:
            raise e

    def GetActiveAll(self):
        try:
            return self.user_repository.ReadActiveAll()
        except Exception as e:
            raise e

    def GetInactiveAll(self):
        try:
            return self.user_repository.ReadInactiveAll()
        except Exception as e:
            raise e
