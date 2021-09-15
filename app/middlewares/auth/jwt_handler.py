import time
from typing import Dict

import jwt
from decouple import config
from app.database.crud.brand import retrieve_brand_from_auth_key


def token_response(token: str):
    return {"access_token": token}


JWT_SECRET = config("secret")


def signJWT(user_id: str) -> Dict[str, str]:
    # Set the expiry time.
    payload = {"user_id": user_id, "expires": time.time() + 36000}
    return token_response(jwt.encode(payload, JWT_SECRET, algorithm="HS256"))


async def decodeJWT(token: str) -> dict:

    # Here tokenization for Brand auth_key as bearer
    if token[0:3] == "pk_":
        to_be_verified_token = await retrieve_brand_from_auth_key(token)
        if token == to_be_verified_token["auth_key"]:
            value = True
            if value:
                isTokenValid = True
        return isTokenValid

    # Here tokenization for general auth as bearer
    try:
        decoded_token = jwt.decode(token.encode(), JWT_SECRET, algorithms=["HS256"])
        print(decoded_token["user_id"])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
