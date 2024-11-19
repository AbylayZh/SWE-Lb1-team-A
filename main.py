from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from internal.handlers.admin import router as home_router
from internal.handlers.buyer import router as buyer_router
from internal.handlers.errors import ValidationErrorHandler
from internal.handlers.farmer import router as farmer_router
from internal.handlers.user import router as user_router
from internal.handlers.image import router as image_router
from internal.handlers.product import router as product_router
from internal.service.services import services
from pkg.middleware.middleware import Authenticate, VerifyAuthentication

app = FastAPI()

app.add_exception_handler(RequestValidationError, ValidationErrorHandler)

# app.add_middleware(LogRequestMiddleware, services=services)
app.add_middleware(Authenticate, services=services)
app.add_middleware(VerifyAuthentication, services=services)

app.include_router(user_router)
app.include_router(farmer_router)
app.include_router(buyer_router)

app.include_router(home_router)

app.include_router(image_router)

app.include_router(product_router)