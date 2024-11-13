import traceback
from http import HTTPStatus

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError


def ClientErrorHandler(err: HTTPStatus, exc, request=None):
    return JSONResponse(
        status_code=err.value,
        content={
            "message": err.phrase,
            "details": exc,
            "request": request,
        }
    )


async def ValidationErrorHandler(req: Request, exc: RequestValidationError):
    body = await req.json()
    body.pop("password", None)
    return ClientErrorHandler(HTTPStatus.UNPROCESSABLE_ENTITY, exc.errors(), body)


def ConflictErrorHandler(req: BaseModel, exc: IntegrityError):
    return ClientErrorHandler(HTTPStatus.CONFLICT, str(exc.orig), req.dict(exclude={"password"}))


def InternalServerHandler(exc: Exception, errorLog):
    errorLog.error(f"Error: {exc}\nTraceback: {traceback.format_exc()}")
    err = HTTPStatus.INTERNAL_SERVER_ERROR

    return JSONResponse(status_code=err.value, content={"message": err.phrase,
                                                        "details": str(exc),
                                                        })
