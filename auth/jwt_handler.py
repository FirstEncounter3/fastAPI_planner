import time
from datetime import datetime
import datetime as dt

from fastapi import HTTPException, status
from jose import jwt, JWTError
from database.connection import Settings

settings = Settings()


def create_access_token(user: str) -> str:
    payload = {"user": user, "expires": time.time() + 3600}

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

    return token


def verify_access_token(token: str) -> dict:
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        expire = data.get("expires")

        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No access token supplied",
            )
        if dt.datetime.now(dt.timezone.utc) > dt.datetime.fromtimestamp(expire, tz=dt.timezone.utc):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Access token has expired"
            )

        return data

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid access token"
        )
