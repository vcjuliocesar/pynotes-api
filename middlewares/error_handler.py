import typing
from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction, RequestResponseEndpoint
from fastapi import FastAPI,status
from fastapi.responses import JSONResponse
from starlette.requests import Request
from starlette.responses import Response

class ErrorHandler(BaseHTTPMiddleware):
    
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)
        
    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
        
            return await call_next(request)
        
        except Exception as error:
        
            return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,content={"error":str(error)})