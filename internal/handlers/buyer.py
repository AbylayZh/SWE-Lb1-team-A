from http import HTTPStatus

from fastapi import APIRouter
from fastapi import Depends, Response
from sqlalchemy.exc import IntegrityError

from internal.handlers.errors import ConflictErrorHandler, InternalServerHandler
from internal.service.services import services, Services
from internal.validators.users import BuyerSignupRequest

router = APIRouter()


@router.post("/signup/buyer")
def BuyerSignupPost(req: BuyerSignupRequest, response: Response, service: Services = Depends(services)):
    try:
        with service.db_session.begin():
            user_id = service.user_service.Register(req)
            service.buyer_service.Register(user_id, req)

            response.status_code = HTTPStatus.SEE_OTHER.value
            return {"message": "OK", "redirect_url": "/user/login"}
    except IntegrityError as err:
        return ConflictErrorHandler(req, err)
    except Exception as err:
        return InternalServerHandler(err, service.loggers.errorLog)
