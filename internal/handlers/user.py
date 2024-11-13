from http import HTTPStatus

from fastapi import APIRouter
from fastapi import Depends, Request, Response

from internal.handlers.errors import InternalServerHandler, ClientErrorHandler
from internal.repository.models.errors import InvalidCredentialsError
from internal.service.services import services, Services
from internal.validators.users import LoginRequest

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
        return ClientErrorHandler(HTTPStatus.UNAUTHORIZED, str(e), req.dict(exclude={"password"}))
    except Exception as e:
        return InternalServerHandler(e, service.loggers.errorLog)


@router.post("/user/logout")
async def UserLogout(req: Request, resp: Response, service: Services = Depends(services)):
    await service.sessions.DeleteCurrentSession(req)

    resp.status_code = HTTPStatus.SEE_OTHER.value
    resp.delete_cookie(key="session_id", secure=True, httponly=True, samesite="lax")
    return {"message": "OK", "redirect_url": "/"}
