from fastapi import Depends
from sqlalchemy.orm import Session

from internal.service.admin.admin import AdminService
from internal.service.buyer.buyer import BuyerService
from internal.service.farmer.farmer import FarmerService
from internal.service.user.user import UserService
from pkg.sessions.store import SessionStore
from pkg.store.sql import NewSQL


class Handlers:
    sessions: SessionStore
    user_service: UserService
    admin_service: AdminService
    farmer_service: FarmerService
    buyer_service: BuyerService

    def __init__(self):
        self.sessions = SessionStore()

    def __call__(self, db: Session = Depends(NewSQL)):
        self.db_session = db
        self.user_service = UserService(db)
        self.admin_service = AdminService(db)
        self.farmer_service = FarmerService(db)
        self.buyer_service = BuyerService(db)

        return self


handlers = Handlers()
