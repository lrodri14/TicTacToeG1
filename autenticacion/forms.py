from django.contrib.auth.forms import UserCreationForm
from .models import JugadorAuth

# Define your forms here.


class JugadorAuthCreationForm(UserCreationForm):
    class Meta:
        model = JugadorAuth
        fields = ('username', 'password1', 'password2', 'email',)
