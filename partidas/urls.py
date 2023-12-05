from django.urls import path, re_path
from partidas import views

urlpatterns = [
    path('', views.Index, name=''),
    path('lista', views.PartidasEnCurso, name='listado'),
    path('privada', views.NuevaPrivada, name='nueva-privada'),
    # path('room/', views.RoomPartida, name='room'),
    path('<str:id>', views.RoomPartida, name='room'),
]