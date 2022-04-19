from email import message
import imp
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User

class UserChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        targetUser = self.scope['url_route']['kwargs']['username']
        authenticatedUser = self.scope["user"]
        print(targetUser, authenticatedUser)

        self.group_name = "{}".format(targetUser)
        self.authenticatedUser = "{}".format(authenticatedUser)

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.channel_layer.group_add(
            self.authenticatedUser,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'recieve_group_message',
                'message': message,
                'username': username
            }
        )
    
    async def recieve_group_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(
             text_data=json.dumps({
            'message': message,
            'username': username
        }))