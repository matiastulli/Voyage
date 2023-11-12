from typing import Any
from fastapi import HTTPException, Request
from functools import wraps

def requires_role(required_role: str):
    def decorator(f):
        @wraps(f)
        async def decorated_function(request: Request, *args, **kwargs) -> Any:
            user = getattr(request.state, 'user', None)
            
            if not user or user["role_description"] != required_role:
                raise HTTPException(status_code=403, detail="Access Denied")

            return await f(request, *args, **kwargs)

        return decorated_function
    return decorator
