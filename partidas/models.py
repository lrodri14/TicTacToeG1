import datetime
from django.db import models
from tictactoeg1 import utils
from django.utils.timezone import now

class Partida(models.Model):
   IDPartida =  models.IntegerField(auto_created=True, primary_key=True, serialize=False)
   CodigoPartida = models.CharField(max_length=255)
   EsPartidaPrivada = utils.MySQLBooleanField()
   JugadorXID = models.IntegerField()
   JugadorOID = models.IntegerField(blank=True, null=True)
   JugadorIDGanador = models.IntegerField(blank=True, null=True)
   IdPartidaEstado = models.IntegerField()
   FechaCreacion = models.DateField(editable=False, default=now)
   class Meta:
        db_table = 'Partidas'
        managed = False

class Jugador(models.Model):
   IDJugador =  models.IntegerField(auto_created=True, primary_key=True, serialize=False)
   Nombre = models.CharField(max_length=255)
   Correo = models.CharField(max_length=255)
   Contraseña = models.CharField(max_length=255)
   class Meta:
        db_table = 'Jugadores'
        managed = False