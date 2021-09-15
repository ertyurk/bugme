from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from .jwt_handler import decodeJWT


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        print("Credentials :", credentials)
        if credentials:
            if not credentials.scheme == "Bearer":
                print("Failed here.")
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid authentication token",
                )

            if not await self.verify_token(credentials.credentials):
                print("Failed here two")
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token or expired token",
                )

            return credentials.credentials
        else:
            print("Failed here three")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid authorization token",
            )

    async def verify_token(self, token: str) -> bool:
        isTokenValid: bool = False
        try:
            payload = await decodeJWT(token)
            # print(payload)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid
