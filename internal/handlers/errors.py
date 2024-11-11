from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def ValidationErrorHandler(request: Request, exc: RequestValidationError):
    body = await request.json()
    body.pop("password", None)

    return JSONResponse(
        status_code=422,
        content={"redirect": False,
                 "message": "INVALID REQUEST BODY",
                 "details": exc.errors(),
                 "request": body,
                 }
    )
