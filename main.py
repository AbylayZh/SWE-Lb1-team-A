from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from internal.handlers.errors import ValidationErrorHandler
from internal.handlers.home import router as home_router
from internal.handlers.user import router as user_router

app = FastAPI()

app.add_exception_handler(RequestValidationError, ValidationErrorHandler)

app.include_router(user_router)
app.include_router(home_router)
