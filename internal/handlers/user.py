from http import HTTPStatus

from fastapi import APIRouter
from fastapi import Depends, Request, Response
from sqlalchemy.exc import IntegrityError

from internal.handlers.errors import InternalServerHandler, ClientErrorHandler, ConflictErrorHandler
from internal.repository.models.errors import InvalidCredentialsError
from internal.service.services import services, Services
from internal.validators.users import LoginRequest, SignupRequest

router = APIRouter()


@router.post("/login")
async def UserLoginPost(req: LoginRequest, resp: Response, service: Services = Depends(services)):
    try:
        user_id = service.user_service.Authenticate(req)
        session_id = await service.sessions.CreateSession(user_id)

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


@router.put("/user/update-password/{id}")
async def UserPasswordUpdate(id: int, req: Request, resp: Response, service: Services = Depends(services)):
    try:
        service.user_service.UpdatePassword(id, req.get("password"))

        resp.status_code = HTTPStatus.SEE_OTHER.value
        return {"message": "OK", "redirect_url": "/"}
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.post("/signup/admin")
def AdminSignupPost(req: SignupRequest, response: Response, service: Services = Depends(services)):
    try:
        with service.db_session.begin():
            user_id = service.user_service.Register(req)
            service.admin_service.Register(user_id)

            response.status_code = HTTPStatus.SEE_OTHER.value
            return {"message": "OK", "redirect_url": "/user/login"}
    except IntegrityError as err:
        return ConflictErrorHandler(req, err)
    except Exception as err:
        return InternalServerHandler(err, service.loggers.errorLog)
