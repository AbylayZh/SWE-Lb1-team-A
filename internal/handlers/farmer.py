from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException
from fastapi import Depends, Response, Request, UploadFile, File
from sqlalchemy.exc import IntegrityError

from internal.handlers.endpoints import url_login, url_farmer_products
from internal.handlers.errors import ConflictErrorHandler, InternalServerHandler
from internal.repository.models.errors import NotFoundError
from internal.service.services import services, Services
from internal.validators.products import ProductRequest
from internal.validators.users import FarmerSignupRequest

router = APIRouter()


@router.post("/signup/farmer")
def FarmerSignupPost(req: FarmerSignupRequest, response: Response,
                     service: Services = Depends(services)):
    try:
        with service.db_session.begin():
            user_id = service.user_service.Register(req)
            farmer_id = service.farmer_service.Register(user_id)
            service.farm_service.Register(farmer_id, req)

            response.status_code = HTTPStatus.SEE_OTHER.value
            return {"message": "OK", "redirect_url": url_login}
    except IntegrityError as err:
        return ConflictErrorHandler(req, err)
    except Exception as err:
        return InternalServerHandler(err, service.loggers.errorLog)


@router.get(url_farmer_products)
def ProductsHandler(req: Request, service: Services = Depends(services)):
    try:
        user = getattr(req.state, 'user', None)
        products = service.product_service.GetAllByFarmerID(user.farmer.id)
        response = {"products": products}

        return service.render(req, response)
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.post(url_farmer_products + "/create")
async def CreateProduct(request: Request, response: Response, service: Services = Depends(services),
                        files: List[UploadFile] = File(...)):
    try:
        form_data = await request.form()

        user = getattr(request.state, 'user', None)
        product_id = service.product_service.Create(user.farmer.id, ProductRequest(**form_data))
        await service.image_service.UploadMultiple(product_id, files)

        response.status_code = HTTPStatus.SEE_OTHER.value
        resp = {"message": "OK", "redirect_url": url_farmer_products + f"/{product_id}"}
        return service.render(request, resp)
    except Exception as err:
        return InternalServerHandler(err, service.loggers.errorLog)


@router.get(url_farmer_products + "/{id}")
def GetProduct(id: int, request: Request, service: Services = Depends(services)):
    try:
        product = service.product_service.Get(id)
        images = service.image_service.GetAllByProductID(product.id)

        resp = {"product": product, "images": images}
        return service.render(request, resp)
    except NotFoundError:
        raise HTTPException(status_code=404)
    except Exception as err:
        return InternalServerHandler(err, service.loggers.errorLog)


@router.delete(url_farmer_products + "/delete/{id}")
def DeleteProduct(id: int, request: Request, response: Response, service: Services = Depends(services)):
    try:
        service.product_service.Delete(id)

        response.status_code = HTTPStatus.SEE_OTHER.value
        resp = {"message": "OK", "redirect_url": url_farmer_products}
        return service.render(request, resp)
    except NotFoundError:
        raise HTTPException(status_code=404)
    except Exception as err:
        return InternalServerHandler(err, service.loggers.errorLog)
