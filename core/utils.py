from django.db import close_old_connections
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from urllib.parse import parse_qs


class TokenAuthMiddleware:
    """
    Custom token auth middleware
    
    """

    def __init__(self, inner):
        # Store the ASGI application we were passed
        self.inner = inner

    def __call__(self, scope):

        # Close old database connections to prevent usage of timed out connections
        close_old_connections()

        # Get the token
        token = parse_qs(scope["query_string"].decode("utf8"))["token"][0]
        decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user = get_user_model().objects.get(id=decoded_data["user_id"])

        # Return the inner application directly and let it run everything else
        return self.inner(dict(scope, user=user))