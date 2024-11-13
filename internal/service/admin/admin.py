from sqlalchemy.orm import Session

from internal.repository.sqlite.users import AdminRepository


class AdminService:
    def __init__(self, db: Session):
        self.admin_repository = AdminRepository(db)

    def Register(self, user_id):
        try:
            self.admin_repository.Create(user_id)
        except Exception as e:
            raise e
