from http import HTTPStatus

from fastapi import APIRouter
from fastapi import Depends, Response, Request
from sqlalchemy.exc import IntegrityError

from internal.handlers.errors import ConflictErrorHandler, InternalServerHandler
from internal.service.services import services, Services
from internal.validators.products import ProductRequest
from internal.validators.users import FarmerSignupRequest

router = APIRouter()


@router.post("/signup/farmer")
def FarmerSignupPost(req: FarmerSignupRequest, response: Response, service: Services = Depends(services)):
    try:
        with service.db_session.begin():
            user_id = service.user_service.Register(req)
            farmer_id = service.farmer_service.Register(user_id, req)
            service.farm_service.Register(farmer_id, req)

            response.status_code = HTTPStatus.SEE_OTHER.value
            return {"message": "OK", "redirect_url": "/user/login"}
    except IntegrityError as err:
        return ConflictErrorHandler(req, err)
    except Exception as err:
        return InternalServerHandler(err, service.loggers.errorLog)


@router.get("/user/farmer/products")
def ProductsHandler(req: Request, service: Services = Depends(services)):
    try:
        user = getattr(req.state, 'user', None)
        products = service.product_service.GetAllByFarmerID(user.farmer.id)
        response = {"products": products}

        return service.render(req, response)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.post("/user/farmer/products/create")
def CreateProduct(request: Request, req: ProductRequest, response: Response, service: Services = Depends(services)):
    try:
        user = getattr(request.state, 'user', None)
        product_id = service.product_service.Create(user.farmer.id, req)

        response.status_code = HTTPStatus.SEE_OTHER.value
        resp = {"message": "OK", "redirect_url": f"/user/farmer/products/{product_id}"}
        return service.render(request, resp)
    except Exception as err:
        return InternalServerHandler(err, service.loggers.errorLog)


@router.get("/user/farmer/products/{id}")
def GetProduct(id: int, request: Request, service: Services = Depends(services)):
    try:
        product = service.product_service.Get(id)

        resp = {"product": product}
        return service.render(request, resp)
    except Exception as err:
        return InternalServerHandler(err, service.loggers.errorLog)


@router.delete("/user/farmer/products/delete/{id}")
def DeleteProduct(id: int, request: Request, response: Response, service: Services = Depends(services)):
    try:
        service.product_service.Delete(id)

        response.status_code = HTTPStatus.SEE_OTHER.value
        resp = {"message": "OK", "redirect_url": f"/user/farmer/products"}
        return service.render(request, resp)
    except Exception as err:
        return InternalServerHandler(err, service.loggers.errorLog)
