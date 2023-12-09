import random
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View
from .models import Partida, Tablero

# Create your views here.


class CrearPartida(View):

    template_name = 'partidas/rooms.html'

    def get(self, request):
        codigo_partida = random.choice(range(10000000, 100000000))
        usuario_creador = request.user
        partida = Partida.objects.create(codigo_partida=codigo_partida, partida_privada=True, jugador_x=usuario_creador)
        Tablero.objects.create(partido=partida)
        context = {'partida': partida, 'user': request.user}
        return render(request, self.template_name, context=context)


class UnirseAPartida(View):

    template_name = 'partidas/rooms.html'

    def post(self, request):
        codigo_partida = request.POST.get('codigo_partida')
        partida = Partida.objects.get(codigo_partida=codigo_partida)
        context = {'partida': partida, 'user': request.user}
        return render(request, self.template_name, context=context)


class Partidas(View):

    template_name = 'partidas/rooms.html'

    def get(self, request):
        partidas = Partida.objects.filter(partida_privada=False)
        context = {'partidas': partidas}
        return render(request, self.template_name, context=context)


class Jugar(View):

    template_name = 'partidas/tablero.html'

    def get(self, request, pk):
        partida = Partida.objects.get(pk=pk)
        tablero = Tablero.objects.get(partido__pk=pk)
        user = request.user
        context = {'partida': partida, 'tablero': tablero, 'user': user, 'jugador_actual_username': partida.jugador_x.username}
        return render(request, self.template_name, context=context)


class Gane(View):
    template_name = 'partidas/resultadoPartida.html'

    def get(self, request, pk):
        partida = Partida.objects.get(pk=pk)
        context = {}

        # Assuming you have a ForeignKey between User and Record
        jugador_x_record = partida.jugador_x.record.first()  # Use .first() to get the first related record
        jugador_0_record = partida.jugador_0.record.first()

        if jugador_x_record and jugador_0_record:
            if partida.jugador_x == partida.jugador_ganador:
                jugador_x_record.puntos += 300
                jugador_x_record.ganes += 1
                jugador_x_record.save()
                jugador_0_record.puntos += 100
                jugador_0_record.perdidas += 1
                jugador_0_record.save()
                context['jugador_ganador'] = partida.jugador_x.username
                context['jugador_perdedor'] = partida.jugador_0.username
            else:
                jugador_0_record.puntos += 300
                jugador_0_record.ganes += 1
                jugador_0_record.save()
                jugador_x_record.puntos += 100
                jugador_x_record.perdidas += 1
                jugador_x_record.save()
                context['jugador_ganador'] = partida.jugador_0.username
                context['jugador_perdedor'] = partida.jugador_x.username
        partida.estado = False
        partida.save()

        return render(request, self.template_name, context=context)


class Empate(View):
    template_name = 'partidas/resultadoPartida2.html'

    def get(self, request, pk):
        partida = Partida.objects.get(pk=pk)
        context = {'partida': partida}

        # Assuming you have a ForeignKey between User and Record
        jugador_x_record = partida.jugador_x.record.first()  # Use .first() to get the first related record
        jugador_0_record = partida.jugador_0.record.first()

        if jugador_x_record and jugador_0_record:
            jugador_x_record.puntos += 200
            jugador_x_record.empates += 1
            jugador_x_record.save()
            jugador_0_record.puntos += 200
            jugador_0_record.empates += 1
            jugador_0_record.save()

        partida.estado = False
        partida.save()
        return render(request, self.template_name, context=context)


class Buscando(View):

    template_name = 'partidas/buscando.html'

    def get(self, request):
        ultima_partida = Partida.objects.filter(Q(jugador_0=None) & ~Q(jugador_x=request.user), partida_privada=False, estado=True).last()
        if ultima_partida is None:
            codigo_partida = random.choice(range(10000000, 100000000))
            usuario_creador = request.user
            partida = Partida.objects.create(codigo_partida=codigo_partida, partida_privada=False, jugador_x=usuario_creador)
            Tablero.objects.create(partido=partida)
            context = {'partida': partida, 'user': request.user, 'mensaje': 'Esperando Oponente...', 'unido': False}
            return render(request, self.template_name, context=context)
        else:
            ultima_partida.jugador_0 = request.user
            ultima_partida.save()
            context = {'partida': ultima_partida, 'user': request.user, 'mensaje': 'Buscando Partida...', 'unido': True}
            return render(request, self.template_name, context=context)


