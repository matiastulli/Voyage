from flask import jsonify, g
from functools import wraps

def requires_role(required_role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = g.get('current_user', None)

            if not user or user["role_description"] != required_role:
                return jsonify({"message": "Acceso denegado"}), 403

            return f(*args, **kwargs)
        return decorated_function
    return decorator
