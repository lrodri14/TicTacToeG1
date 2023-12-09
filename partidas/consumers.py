import json
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Mensaje, Partida

User = get_user_model()

# Define your consumers here.


class PartidaRoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.pk = self.scope['url_route']['kwargs']['pk']
        self.room_group_name = f"partida_{self.pk}"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        pass

    @database_sync_to_async
    def crear_mensaje(self, data):
        partida = Partida.objects.get(codigo_partida=data.get('codigo'))
        usuario = User.objects.get(username=data.get('usuario'))
        return Mensaje.objects.create(mensaje=data.get('mensaje'), partida=partida, enviado_por=usuario)

    @database_sync_to_async
    def asignar_jugador(self, data):
        codigo_partida = data.get('codigo')
        usuario = data.get('usuario')
        usuario_recolectado = User.objects.get(username=usuario)
        partida = Partida.objects.get(codigo_partida=codigo_partida)
        if (partida.jugador_x and partida.jugador_x.username == usuario_recolectado.username) or \
                (partida.jugador_0 and partida.jugador_0.username == usuario_recolectado.username):
            return {'jugador_x': partida.jugador_x.username if partida.jugador_x else '',
                    'jugador_0': partida.jugador_0.username if partida.jugador_0 else ''}
        elif partida.jugador_x:
            partida.jugador_0 = usuario_recolectado
        else:
            partida.jugador_x = usuario_recolectado
        partida.save()
        return {'jugador_x': partida.jugador_x.username, 'jugador_0': partida.jugador_0.username}

    @database_sync_to_async
    def remover_jugador(self, data):
        codigo_partida = data.get('codigo')
        usuario = data.get('usuario')
        usuario_recolectado = User.objects.get(username=usuario)
        partida = Partida.objects.get(codigo_partida=codigo_partida)
        if partida.jugador_x == usuario_recolectado:
            partida.jugador_x = None
        else:
            partida.jugador_0 = None
        partida.save()
        return {'jugador_x': partida.jugador_x.username if partida.jugador_x else '',
                'jugador_0': partida.jugador_0.username if partida.jugador_0 else ''}

    async def unirse(self, data):
        jugadores_actualizados = await self.asignar_jugador(data)
        jugadores_actualizados['tipo'] = 'usuario_unido'

        # Send the message to the entire group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_user_update',
                'message': json.dumps(jugadores_actualizados),
            }
        )

    async def abandonar(self, data):
        jugadores_actualizados = await self.remover_jugador(data)
        jugadores_actualizados['tipo'] = 'usuario_abandono'

        # Send the message to the entire group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_user_update',
                'message': json.dumps(jugadores_actualizados),
            }
        )

    async def mensaje(self, data):
        mensaje_enviar = await self.crear_mensaje(data)
        mensaje_enviar = {'mensaje': mensaje_enviar.mensaje, 'tipo': 'mensaje'}

        # Send the message to the entire group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_user_update',
                'message': json.dumps(mensaje_enviar),
            }
        )

    async def iniciar_partida(self):
        mensaje_enviar = {'tipo': 'iniciar'}

        # Send the message to the entire group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_user_update',
                'message': json.dumps(mensaje_enviar),
            }
        )

    async def send_user_update(self, event):
        # Send the message to the WebSocket
        await self.send(text_data=event['message'])

    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        tipo = text_data_json.get('tipo')

        if tipo == 'unirse':
            await self.unirse(text_data_json)
        elif tipo == 'abandonar':
            await self.abandonar(text_data_json)
        elif tipo == 'iniciar':
            await self.iniciar_partida()
        else:
            await self.mensaje(text_data_json)


class PartidaConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.pk = self.scope['url_route']['kwargs']['pk']
        self.room_group_name = f"partida_jugar_{self.pk}"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        pass

    @database_sync_to_async
    def agregar_posicion(self, marca, posicion):
        p = Partida.objects.get(pk=self.pk)
        print(p.jugador_x.username)
        tablero = p.tablero.all().first()

        if posicion == '1' and not tablero.pos_1:
            tablero.pos_1 = marca
        elif posicion == '2' and not tablero.pos_2:
            tablero.pos_2 = marca
        elif posicion == '3' and not tablero.pos_3:
            tablero.pos_3 = marca
        elif posicion == '4' and not tablero.pos_4:
            tablero.pos_4 = marca
        elif posicion == '5' and not tablero.pos_5:
            tablero.pos_5 = marca
        elif posicion == '6' and not tablero.pos_6:
            tablero.pos_6 = marca
        elif posicion == '7' and not tablero.pos_7:
            tablero.pos_7 = marca
        elif posicion == '8' and not tablero.pos_8:
            tablero.pos_8 = marca
        elif posicion == '9' and not tablero.pos_9:
            tablero.pos_9 = marca

        tablero.save()

        # Now reload the board
        tablero.refresh_from_db()

        board = [
            tablero.pos_1, tablero.pos_2, tablero.pos_3,
            tablero.pos_4, tablero.pos_5, tablero.pos_6,
            tablero.pos_7, tablero.pos_8, tablero.pos_9
        ]

        for i in range(3):
            if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] and board[i * 3] != '':
                if board[i * 3] == 'X':
                    p.jugador_ganador = p.jugador_x
                else:
                    p.jugador_ganador = p.jugador_0
                p.save()
                return {'tipo': 'gane', 'ganador':  p.jugador_ganador.username}

        # Check columns
        for i in range(3):
            if board[i] == board[i + 3] == board[i + 6] and board[i] != '':
                if board[i + 3] == 'X':
                    p.jugador_ganador = p.jugador_x
                else:
                    p.jugador_ganador = p.jugador_0
                p.save()
                return {'tipo': 'gane', 'ganador': p.jugador_ganador.username}

        # Check diagonals
        if board[0] == board[4] == board[8] and board[0] != '':
            if board[0] == 'X':
                p.jugador_ganador = p.jugador_x
            else:
                p.jugador_ganador = p.jugador_0
            p.save()
            return {'tipo': 'gane', 'ganador': p.jugador_ganador.username}
        if board[2] == board[4] == board[6] and board[2] != '':
            if board[2] == 'X':
                p.jugador_ganador = p.jugador_x
            else:
                p.jugador_ganador = p.jugador_0
            p.save()
            return {'tipo': 'gane', 'ganador': p.jugador_ganador.username}

        if board[0] != '' and board[1] != '' and board[2] != '' and \
            board[3] != '' and board[4] != '' and board[5] != '' and board[6] != '' and \
                board[7] != '' and board[8] != '':
            return {'tipo': 'empate'}

        return {'tipo': 'continuacion', 'tabla': board,
                'jugador_actual': 'X' if marca == '0' else '0',
                'jugador_actual_username': p.jugador_x.username if marca == '0' else p.jugador_0.username}

    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        marca = text_data_json.get('marcador')
        posicion = text_data_json.get('posicion')
        nuevas_pos = await self.agregar_posicion(marca, posicion)
        print(nuevas_pos)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_user_update',
                'message': json.dumps(nuevas_pos),
            }
        )

    async def send_user_update(self, event):
        # Send the message to the WebSocket
        await self.send(text_data=event['message'])


class BuscandoConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.pk = self.scope['url_route']['kwargs']['pk']
        self.room_group_name = f"buscando_{self.pk}"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        pass

    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        unido = text_data_json.get('unido')
        if unido:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'send_user_update',
                    'message': json.dumps({'redirigir': True}),
                }
            )

    async def send_user_update(self, event):
        # Send the message to the WebSocket
        await self.send(text_data=event['message'])

