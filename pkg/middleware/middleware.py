from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


class Authenticate(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Custom logic before handling the request
        print("Request received:", request.method, request.url)

        response = await call_next(request)

        # Custom logic after handling the request
        response.headers['X-Custom-Header'] = 'MyCustomValue'
        return response


class RequireAuthentication(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Custom logic before handling the request
        print("Request received:", request.method, request.url)

        response = await call_next(request)

        # Custom logic after handling the request
        response.headers['X-Custom-Header'] = 'MyCustomValue'
        return response
