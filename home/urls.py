from django.urls import path
from .views import *

# Define your urls here.

app_name = 'home'

urlpatterns = [
    path('', Cargando.as_view(), name='cargando'),
    path('home', Home.as_view(), name='home'),
]
