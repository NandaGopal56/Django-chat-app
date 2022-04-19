"""
ASGI config for DjangoChatApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import room.routing as roomRouting
import userchat.routing as userchatRouting
import userchat
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoChatApp.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            roomRouting.websocket_urlpaterns +
            userchatRouting.websocket_urlpaterns,
        )
    )}
)
