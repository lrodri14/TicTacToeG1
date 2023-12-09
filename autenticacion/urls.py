from django.urls import path
from .views import *

# Define your urls here.
app_name = 'autenticacion'

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('sign-up', SignUp.as_view(), name='sign-up'),
    path('logout', Logout.as_view(), name='logout'),
]