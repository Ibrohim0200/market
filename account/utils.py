from datetime import timedelta
import jwt
from market.settings import SECRET_KEY
from django.utils import timezone

def create_token(user_id):
    now = timezone.now()
    access_exp = int((now + timedelta(minutes=5)).timestamp())
    refresh_exp = int((now + timedelta(days=7)).timestamp())
    iat = int(now.timestamp())

    payload_access = {
        "user_id": user_id,
        "exp": access_exp,
        "iat": iat,
        "token_type": "access"
    }

    payload_refresh = {
        "user_id": user_id,
        "exp": refresh_exp,
        "iat": iat,
        "token_type": "refresh"
    }

    access_token = str(jwt.encode(payload_access, SECRET_KEY, algorithm='HS256'))
    refresh_token = str(jwt.encode(payload_refresh, SECRET_KEY, algorithm='HS256'))

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }

def verify_token(token, secret=SECRET_KEY, expected_type="access"):
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        if payload.get("token_type") != expected_type:
            return None
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
