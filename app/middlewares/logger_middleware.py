from starlette.middleware.base import BaseHTTPMiddleware
from app.controllers.auth_controller import AuthController

def create_auth_middleware(app):
    auth_controller = AuthController()

    class AuthMiddleware(BaseHTTPMiddleware):
        async def dispatch(self, request, call_next):
            user = auth_controller.get_current_user(request)

            # Attach the user to the request context
            request.state.current_user = user

            response = await super().dispatch(request, call_next)
            return response

    return AuthMiddleware(app)
