from http import HTTPStatus

from fastapi import APIRouter
from fastapi import Depends, Response, Request
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


@router.get("/user/buyer/products")
def ProductsHandler(req: Request, service: Services = Depends(services)):
    """
    try:
        user = getattr(req.state, 'user', None)
        products = service.product_service.GetAllByFarmerID(user.farmer.id)
        response = {"products": products}

        return service.render(req, response)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)
    """


@router.get("/user/buyer/products/{id}")
def GetProduct(id: int, request: Request, service: Services = Depends(services)):
    try:
        product = service.product_service.Get(id)
        images = service.image_service.GetAllByProductID(product.id)

        resp = {"product": product, "images": images}
        return service.render(request, resp)
    except Exception as err:
        return InternalServerHandler(err, service.loggers.errorLog)
