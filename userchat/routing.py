import imp
from django.urls import path
from . import consumers

websocket_urlpaterns = [
    path('uws/<str:username>/', consumers.UserChatConsumer.as_asgi()),
]