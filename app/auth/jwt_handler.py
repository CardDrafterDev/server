import jwt
from app.utils.env import get_var

secret = get_var("JWT_SECRET")

def decrypt_jwt(token: str) -> dict[str, dict[str, any]]:
    decoded_data = jwt.decode(
        jwt=token,
        key=secret,
        algorithms=["HS256"]
    )
    
    return decoded_data


def encrypt_jwt(data: dict) -> str:
    encoded_data = jwt.encode(
        payload=data,
        key=secret,
        algorithm="HS256"
    )

    return encoded_data
