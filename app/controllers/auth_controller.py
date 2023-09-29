import jwt

class AuthController:
    
    def get_current_user(self, token: str):
        """
        Get the current user from the decoded token.
        """
        if token:
            token = token.replace("Bearer ", "")
            try:
                decoded_token = jwt.decode(token, options={"verify_signature": False})
                return decoded_token
            except jwt.ExpiredSignatureError:
                # Handle token expiration here
                return None
            except jwt.PyJWTError as ex:
                # Handle token decoding error here
                return None
        else:
            return None
        
auth_controller = AuthController()