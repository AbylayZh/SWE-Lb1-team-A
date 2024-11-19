import traceback
from http import HTTPStatus

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError

from internal.config.logger import error_log


def ClientErrorHandler(err: HTTPStatus, exc, user=None, request=None):
    return JSONResponse(
        status_code=err.value,
        content={
            "message": err.phrase,
            "details": exc,
            "request": request,
            "auth_user": user,
        }
    )


async def ValidationErrorHandler(req: Request, exc: RequestValidationError, user=None):
    try:
        body = await req.json()
        body.pop("password", None)

        return ClientErrorHandler(HTTPStatus.UNPROCESSABLE_ENTITY, exc.errors(), user, body)
    except Exception as e:
        return InternalServerHandler(e, error_log)


def ConflictErrorHandler(req: BaseModel, exc: IntegrityError, user=None):
    return ClientErrorHandler(HTTPStatus.CONFLICT, str(exc.orig), user, req.dict(exclude={"password"}))


def InternalServerHandler(exc: Exception, errorLog):
    errorLog.error(f"Error: {exc}\nTraceback: {traceback.format_exc()}")
    err = HTTPStatus.INTERNAL_SERVER_ERROR

    return JSONResponse(status_code=err.value, content={"message": err.phrase,
                                                        "details": str(exc),
                                                        })
