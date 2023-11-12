import json
from datetime import datetime
from loguru import logger
from fastapi import Request
from starlette.types import Message
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from app.controllers.database_controller import database_controller
from app.schemas.kpi import Log

class ActivityLogger(BaseHTTPMiddleware):
    
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        logger.info("Log activity middleware")
        
        body = await request.body()
        body_data = {}
        if body:
            try:
                body_data = json.loads(body.decode('utf-8'))
            except json.JSONDecodeError as e:
                logger.error(f"Error decoding JSON: {e}")
        
        user = getattr(request.state, 'user', None)
        body_data = {}
        
        if user:
            with database_controller.DatabaseSession(database_controller) as session:
                log = Log(
                    user_mail=user["mail"],
                    body_data=body_data,
                    host=request.client.host if request.client else None,
                    route=request.url.path,
                    date=datetime.now()
                )

                session.add(log)
                session.flush()
                logger.info(f"User {log.user_mail} accessed {log.route} at {log.date}")

        await self.set_body(request, body)

        response = await call_next(request)
        return response

    async def set_body(self, request: Request, body: bytes):
        receive_ = await self.get_receive(body)

        async def receive() -> Message:
            return await receive_()

        request._receive = receive

    async def get_receive(self, body: bytes):
        async def receive() -> Message:
            return {"type": "http.request", "body": body, "more_body": False}
        return receive