from jwt import encode, decode
from datetime import datetime, timedelta
from utils.settings import Settings

settings = Settings()


def create_token(data: dict) -> dict:
    payload = add_expiration_date(data)

    token: str = encode(payload, key=settings.MY_SECRET_KEY, algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    data: dict = decode(token, key=settings.MY_SECRET_KEY, algorithms=["HS256"])

    return data


def calculate_token_expiration():
    return datetime.utcnow() + timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES)


def add_expiration_date(data: dict):
    to_encode = data.copy()
    to_encode['exp'] = calculate_token_expiration()

    return to_encode
