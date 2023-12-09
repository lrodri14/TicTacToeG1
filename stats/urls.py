from django.urls import path
from .views import Estadisticas

# Define your urls here.
app_name = 'stats'

urlpatterns = [
    path('', Estadisticas.as_view(), name='stats')
]