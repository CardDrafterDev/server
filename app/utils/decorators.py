from app.auth.methods import validate_token

from fastapi import status, Request
from functools import wraps



def protected(func):
    """
    Decorator function that adds authentication to a route.

    Parameters:
    - func (Callable): The route handler function to be decorated.

    Returns:
    - wrapper (Callable): The wrapper function that adds authentication logic to the route.
    """
    # Dont forget to pass request as an argument:
    # e.g. @protected
    #      async def function(request: Request):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        token = request.cookies.get("jwt-token")
        if token == None:
            return {
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Unauthorized"
            }
        if validate_token(token)["result"]:
            return await func(request, *args, **kwargs)
        
    return wrapper
