import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

application = ProtocolTypeRouter(
    {
        "websockets": AuthMiddlewareStack(
            URLRouter(
                "",  # router
            )
        ),  # need parameter
        # Just HTTP for now. (We can add other protocols later.)
    }
)
