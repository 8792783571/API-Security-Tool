import jwt

SECRET = "mysecretkey"


def validate_token(token):

    try:

        token = token.replace("Bearer ", "")

        jwt.decode(
            token,
            SECRET,
            algorithms=["HS256"]
        )

        return True

    except Exception:
        return False
