from django.urls import path
from .views import Menu

# Define your urls here.

app_name = 'menu'

urlpatterns = [
    path('', Menu.as_view(), name='menu')
]
