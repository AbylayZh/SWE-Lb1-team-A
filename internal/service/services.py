from fastapi import Depends, Request
from sqlalchemy.orm import Session

from internal.config.logger import Logger, loggers
from internal.service.admin.admin import AdminService
from internal.service.buyer.buyer import BuyerService
from internal.service.farm.farm import FarmService
from internal.service.farmer.farmer import FarmerService
from internal.service.product.product import ProductService
from internal.service.user.json import UserJson
from internal.service.user.user import UserService
from pkg.sessions.store import SessionStore
from pkg.store.sql import NewSQL


class Services:
    session_limit = 1
    sessions: SessionStore
    user_service: UserService
    admin_service: AdminService
    farmer_service: FarmerService
    buyer_service: BuyerService

    def __init__(self, logger: Logger):
        self.sessions = SessionStore()
        self.loggers = logger

    def __call__(self, db: Session = Depends(NewSQL)):
        self.db_session = db
        self.user_service = UserService(db)
        self.admin_service = AdminService(db)
        self.farmer_service = FarmerService(db)
        self.farm_service = FarmService(db)
        self.buyer_service = BuyerService(db)
        self.product_service = ProductService(db)

        return self

    def render(self, req: Request, response):
        response["authenticated_user"] = UserJson(getattr(req.state, 'user', None))
        return response


services = Services(loggers)
