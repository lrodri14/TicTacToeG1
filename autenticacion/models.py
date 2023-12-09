from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class JugadorAuth(AbstractUser):
    pass


class Record(models.Model):
    puntos = models.IntegerField(blank=False, null=False, default=0)
    ganes = models.IntegerField(blank=False, null=False, default=0)
    perdidas = models.IntegerField(blank=False, null=False, default=0)
    empates = models.IntegerField(blank=False, null=False, default=0)
    jugador = models.ForeignKey(to=JugadorAuth, on_delete=models.CASCADE, related_name='record')

