# routing.py
from django.urls import path

from sockets.consumers import ChatConsumer
# from . import consumers

websocket_urlpaterns = [
    path('juegos/<str:room_name>/', ChatConsumer.as_asgi()),
    path('ws/juegos/<str:room_name>/', ChatConsumer.as_asgi()),
]