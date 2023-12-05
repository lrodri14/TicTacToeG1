import json
from pprint import pprint

from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'juego_%s' %self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive message from WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # pprint(vars(self))

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': message,
                'custom': text_data_json['custom'],
                'sender_channel_name': self.channel_name
            }
        )

    def chat_message(self, event, type='nuevo_observador'):
        print("EVENT TRIGERED")

    async def chat_message(self, event):
        # Send message to WebSocket
        message = event['message']

         # send to everyone else than the sender
        if self.channel_name != event['sender_channel_name']:
            await self.send(text_data=json.dumps(event))

        # await self.send(text_data=json.dumps({
        #     'message': message
        # }))