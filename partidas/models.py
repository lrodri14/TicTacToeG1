from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Partida(models.Model):
    codigo_partida = models.CharField(max_length=8, blank=False, null=False)
    partida_privada = models.BooleanField(default=False, blank=False, null=False)
    jugador_x = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='jugador_x')
    jugador_0 = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='jugador_0')
    jugador_ganador = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='jugador_ganador')
    estado = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        db_table = 'Partida'
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'


class Tablero(models.Model):
    pos_1 = models.CharField(max_length=1, blank=True, null=False, default='')
    pos_2 = models.CharField(max_length=1, blank=True, null=False, default='')
    pos_3 = models.CharField(max_length=1, blank=True, null=False, default='')
    pos_4 = models.CharField(max_length=1, blank=True, null=False, default='')
    pos_5 = models.CharField(max_length=1, blank=True, null=False, default='')
    pos_6 = models.CharField(max_length=1, blank=True, null=False, default='')
    pos_7 = models.CharField(max_length=1, blank=True, null=False, default='')
    pos_8 = models.CharField(max_length=1, blank=True, null=False, default='')
    pos_9 = models.CharField(max_length=1, blank=True, null=False, default='')
    partido = models.ForeignKey(Partida, on_delete=models.CASCADE, related_name='tablero')

    class Meta:
        db_table = 'Tablero'
        verbose_name = 'Tablero'
        verbose_name_plural = 'Tableros'


class Mensaje(models.Model):
    mensaje = models.CharField(max_length=255, blank=False, null=False, default='')
    partida = models.ForeignKey(to=Partida, on_delete=models.CASCADE, blank=False, null=True)
    enviado_por = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False, null=True)

