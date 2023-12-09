from django.urls import path
from .consumers import *

# Define consumer urls here.

websocket_urlpatterns = [
    path('ws/partidas/jugar/<int:pk>', PartidaConsumer.as_asgi()),
    path('ws/partida/<int:pk>', PartidaRoomConsumer.as_asgi()),
    path('ws/partida/buscando/<int:pk>', BuscandoConsumer.as_asgi()),
]

