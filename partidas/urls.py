from django.urls import path, include
from .views import Partidas, CrearPartida, UnirseAPartida, Jugar, Gane, Empate, Buscando

# Define your urls here.
app_name = 'partidas'

urlpatterns = [
    path('', Partidas.as_view(), name='partidas'),
    path('crear_partida', CrearPartida.as_view(), name='crear_partida'),
    path('entrar_partida', UnirseAPartida.as_view(), name='entrar_partida'),
    path('jugar/<int:pk>/', Jugar.as_view(), name='jugar'),
    path('gane/<int:pk>/', Gane.as_view(), name='gane'),
    path('empate/<int:pk>/', Empate.as_view(), name='jugar'),
    path('buscando/', Buscando.as_view(), name='buscando'),
]