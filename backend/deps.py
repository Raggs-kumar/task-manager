from fastapi import Header, HTTPException
from auth import decode_token

def get_current_user(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]
    except:
        raise HTTPException(401, "Invalid token format")

    payload = decode_token(token)
    if not payload:
        raise HTTPException(401, "Invalid or expired token")

    return payload["user_id"]