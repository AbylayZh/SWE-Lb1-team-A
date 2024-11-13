from http import HTTPStatus

from fastapi import Request, FastAPI
from sqlalchemy.exc import SQLAlchemyError
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from internal.handlers.errors import InternalServerHandler
from internal.repository.models.errors import RoleAuthenticationError, UserAuthenticationError
from internal.service.services import Services


class BaseServiceMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI, services: Services):
        super().__init__(app)
        self.services = services


class LogRequestMiddleware(BaseServiceMiddleware):
    async def dispatch(self, request: Request, call_next):
        self.services.loggers.infoLog.info(f"{request.client.host} - {request.method} {request.url}")
        response = await call_next(request)
        return response


class Authenticate(BaseServiceMiddleware):
    async def dispatch(self, req: Request, call_next):
        error_log = self.services.loggers.errorLog
        session = await self.services.sessions.GetCurrentSession(req)
        if session:
            user_id = session.get("user_id")
            if user_id:
                try:
                    user = self.services.user_service.Get(user_id)
                    if user:
                        if user.admin:
                            user.role = "admin"
                        elif user.farmer:
                            user.role = "farmer"
                        elif user.buyer:
                            user.role = "buyer"
                        else:
                            return InternalServerHandler(RoleAuthenticationError(), error_log)

                        req.state.user = user
                    else:
                        return InternalServerHandler(UserAuthenticationError(), error_log)
                except SQLAlchemyError as e:
                    return InternalServerHandler(e, error_log)

        response = await call_next(req)
        return response


class VerifyAuthentication(BaseServiceMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Extract user from request state (set in earlier middleware)
        user = getattr(request.state, 'user', None)

        # If user is authenticated
        if user:
            # Prevent logged-in users from accessing /login or /signup
            if request.url.path.startswith("/login") or request.url.path.startswith("/signup"):
                return JSONResponse(
                    status_code=HTTPStatus.FORBIDDEN.value,
                    content={"message": HTTPStatus.FORBIDDEN.phrase}
                )

            # Ensure user can access only role-specific endpoints
            if not request.url.path.startswith(f"/user/{user.role}"):
                return JSONResponse(
                    status_code=HTTPStatus.FORBIDDEN.value,
                    content={"message": HTTPStatus.FORBIDDEN.phrase}
                )
        else:
            # Prevent unauthenticated users from accessing /user endpoints
            if request.url.path.startswith("/user"):
                return JSONResponse(
                    status_code=HTTPStatus.UNAUTHORIZED.value,
                    content={"message": HTTPStatus.UNAUTHORIZED.phrase}
                )

        # If no issues, continue with the request processing
        response = await call_next(request)
        return response
