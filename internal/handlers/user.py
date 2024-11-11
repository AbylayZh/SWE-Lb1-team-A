from http import HTTPStatus

from fastapi import APIRouter
from fastapi import Depends, Request, Response

from internal.handlers.handler import Handlers, handlers
from internal.repository.models.errors import InvalidCredentialsErr, SQLConstraintError, Error
from internal.validators.users import LoginRequest, FarmerSignupRequest, BuyerSignupRequest

router = APIRouter()


@router.post("/user/farmer/signup")
async def FarmerSignupPost(req: FarmerSignupRequest, response: Response, handler: Handlers = Depends(handlers)):
    try:
        with handler.db_session.begin():
            user_id = handler.user_service.Register(req)
            handler.farmer_service.Register(user_id, req)

            response.status_code = HTTPStatus.SEE_OTHER.value
            return {"redirect": True, "url": "/user/login", "message": "OK"}
    except Error as err:
        response.status_code = err.http_status

        if isinstance(err, SQLConstraintError):
            return {"redirect": False, "message": err.message,
                    "request": req.dict(exclude={"password"})}

        return {"redirect": False, "message": err.message}


@router.post("/user/buyer/signup")
async def BuyerSignupPost(req: BuyerSignupRequest, response: Response, handler: Handlers = Depends(handlers)):
    try:
        with handler.db_session.begin():
            user_id = handler.user_service.Register(req)
            handler.buyer_service.Register(user_id, req)

            response.status_code = HTTPStatus.SEE_OTHER.value
            return {"redirect": True, "url": "/user/login", "message": "OK"}
    except Error as err:
        response.status_code = err.http_status

        if isinstance(err, SQLConstraintError):
            return {"redirect": False, "message": err.message,
                    "request": req.dict(exclude={"password"})}

        return {"redirect": False, "message": err.message}


@router.post("/user/login")
async def UserLoginPost(req: LoginRequest, response: Response, handler: Handlers = Depends(handlers)):
    try:
        user = handler.user_service.Authenticate(req)
    except Error as err:
        response.status_code = err.http_status

        if err is InvalidCredentialsErr:
            return {"redirect": False, "message": err.message, "request": req.dict(exclude={"password"})}

        return {"redirect": False, "message": err.message}

    session_id = await handlers.sessions.CreateSession(user)

    response.status_code = HTTPStatus.SEE_OTHER.value
    response.set_cookie(key="session_id", value=session_id, secure=True, httponly=True, samesite="lax")
    return {"redirect": True, "url": "/", "message": "OK"}


@router.post("/user/logout")
async def UserLogout(req: Request, response: Response, handler: Handlers = Depends(handlers)):
    await handler.sessions.DeleteCurrentSession(req)

    response.status_code = HTTPStatus.SEE_OTHER.value
    response.delete_cookie(key="session_id", secure=True, httponly=True, samesite="lax")
    return {"redirect": True, "url": "/", "message": "OK"}
