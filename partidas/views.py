import json
import random, string
from socket import create_connection
import time
from django.shortcuts import get_object_or_404, render, redirect
from partidas.models import Jugador, Partida
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# Create your views here.
def PartidasEnCurso(request):
  data = Partida.objects.all()
  return render(request, 'lista.html', context={"data":data})

def NuevaPrivada(request):

  # TODO: REEMPLAZAR POR USUARIO DE LA SESION
  idUsuarioLogeado = 2

  # Crear nueva partida privada
  partida = Partida()
  partida.CodigoPartida = ''.join(random.choices(string.ascii_letters + string.digits, k=6)).upper()
  partida.EsPartidaPrivada = True
  partida.JugadorXID = idUsuarioLogeado
  partida.IdPartidaEstado = 1
  partida.save()
  
  # return redirect(reverse('room', args=["aaa"]))
  return redirect('room', id=partida.CodigoPartida)

def RoomPartida(request, id):

  # TODO: REEMPLAZAR POR USUARIO DE LA SESION
  idUsuarioLogeado = 3

  partida = get_object_or_404(Partida, CodigoPartida=id)
  jugadorX = get_object_or_404(Jugador, IDJugador=partida.JugadorXID)
  jugadores = [jugadorX.Nombre]
  partidaPorEmpezar = False

  if partida.JugadorOID == None:
    partidaPorEmpezar = True
    if (jugadorX.IDJugador != idUsuarioLogeado):
      partida.JugadorOID = idUsuarioLogeado
      partida.IdPartidaEstado = 2
      partida.save()

  if partida.JugadorOID != None:
    jugadores.append(Jugador.objects.get(IDJugador=partida.JugadorOID).Nombre)

  data = {
    "esPrivada": partida.EsPartidaPrivada,
    "codigoPartida": partida.CodigoPartida,
    "jugadores": jugadores,
    "yaEmpezada": len(jugadores) > 1,
  }

  if partidaPorEmpezar:
    return render(request, 'room.html', context={"data": data})
  
  return render(request, 'tablero.html', context={"data": data})

def Index(request):
#   data = Partidas.objects.all()
  return render(request, 'menu.html')