from http import HTTPStatus

from fastapi import APIRouter
from fastapi import Depends, Request, Response
from fastapi.responses import RedirectResponse
from sqlalchemy.exc import IntegrityError

from internal.handlers.endpoints import url_login, url_pending_users, url_farmer_products, url_buyer_products
from internal.handlers.errors import InternalServerHandler, ClientErrorHandler, ConflictErrorHandler
from internal.repository.models.errors import InvalidCredentialsError
from internal.service.services import services, Services
from internal.validators.users import LoginRequest, SignupRequest

router = APIRouter()


@router.post(url_login)
async def UserLoginPost(req: LoginRequest, resp: Response, service: Services = Depends(services)):
    try:
        user = service.user_service.Authenticate(req)
        session_id = await service.sessions.CreateSession(user.id)

        resp.status_code = HTTPStatus.SEE_OTHER.value
        resp.set_cookie(key="session_id", value=session_id, secure=True, httponly=True, samesite="lax")
        return {"message": "OK", "redirect_url": "/"}
    except InvalidCredentialsError as e:
        return ClientErrorHandler(err=HTTPStatus.UNAUTHORIZED, exc=str(e), request=req.dict(exclude={"password"}))
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.post("/user/logout")
async def UserLogout(req: Request, resp: Response, service: Services = Depends(services)):
    await service.sessions.DeleteCurrentSession(req)

    resp.status_code = HTTPStatus.SEE_OTHER.value
    resp.delete_cookie(key="session_id", secure=True, httponly=True, samesite="lax")
    return {"message": "OK", "redirect_url": "/"}


@router.post("/signup/admin")
def AdminSignupPost(req: SignupRequest, response: Response, service: Services = Depends(services)):
    try:
        with service.db_session.begin():
            user_id = service.user_service.Register(req)
            service.admin_service.Register(user_id)

            response.status_code = HTTPStatus.SEE_OTHER.value
            return {"message": "OK", "redirect_url": url_login}
    except IntegrityError as err:
        return ConflictErrorHandler(req, err)
    except Exception as err:
        return InternalServerHandler(err, service.loggers.errorLog)


@router.get("/")
def Home(request: Request):
    user = getattr(request.state, 'user', None)
    if user:
        if user.role == "admin":
            return RedirectResponse(url=url_pending_users)

        if user.role == "farmer":
            return RedirectResponse(url=url_farmer_products)

        if user.role == "buyer":
            return RedirectResponse(url=url_buyer_products)

    return RedirectResponse(url=url_login)
