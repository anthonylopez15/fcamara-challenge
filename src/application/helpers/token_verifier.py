from functools import wraps

from src import env

token_fake = env.TOKEN_FAKE


def token_verify(function: callable) -> callable:
    @wraps(function)
    def decorated(*arg, **kwargs):
        request = kwargs["request"]
        response = kwargs["response"]
        raw_token = request.headers.get("Authorization")

        if not raw_token:
            error = {"message": "Bad Request"}
            response.status_code = 400
            return {"error": error}

        try:
            token = raw_token.split()[1]
            is_valid_token = token == token_fake

        except Exception as e:
            print(e)
            error = {"message": "Token is invalid"}
            response.status_code = 401
            return {"error": error}

        if not is_valid_token:
            error = {"message": "User Unauthorized"}
            response.status_code = 401
            return {"error": error}

        return function(*arg, **kwargs)

    return decorated
