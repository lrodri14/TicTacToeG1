from django.urls import path
from .views import Info

# Define your urls here.
app_name = 'info'

urlpatterns = [
    path('', Info.as_view(), name='info')
]