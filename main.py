from dotenv import load_dotenv
from loguru import logger

from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.middlewares.activity_logger_middleware import ActivityLogger
from app.middlewares.authentication_middleware import AuthenticateRequest
from app.routes.user_routes import router as user_router
from app.routes.role_routes import router as role_router
from app.routes.event_routes import router as event_router

load_dotenv()

app = FastAPI()

app.add_middleware(ActivityLogger)
app.add_middleware(AuthenticateRequest)

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTP exception occurred: {exc.detail}, Status code: {exc.status_code}")
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation error: {exc}, Path: {request.url.path}")
    return JSONResponse(status_code=422, content={"error": f"Validation error: {exc}"})

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Generic error occurred at {request.url}: {exc}")
    return JSONResponse(status_code=500, content={"error": f"Generic error at {request.url.path}: {exc}"})

app.include_router(user_router, prefix='/user')
app.include_router(role_router, prefix='/role')
app.include_router(event_router, prefix='/event')
