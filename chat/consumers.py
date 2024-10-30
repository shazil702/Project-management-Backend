from channels.generic.websocket import AsyncWebsocketConsumer
import json
from Authentication.models import User
from asgiref.sync import sync_to_async
from .models import ChatMessage, ChatRoom

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        print(f'Connecting to chat group: {self.room_group_name}')
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        print(f'Connected to chat group: {self.channel_name}')
    
    async def disconnect(self, close_code):
        print(f'Disconnecting from chat group: {self.room_group_name}')
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print(f'Disconnected from chat group: {self.channel_name}')
    
    async def receive(self, text_data):
        print(f'Received message from {self.channel_name}: {text_data}')
        data = json.loads(text_data)
        username = data['username']
        message_body = data['body']
        user = await sync_to_async(User.objects.get)(username=username)
        room, created = await sync_to_async(ChatRoom.objects.get_or_create)(name=self.room_name)
        message = await sync_to_async(ChatMessage.objects.create)(
            room=room,
            user=user,
            body=message_body
        )
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "message": message_body,
                "username": username
            }
        )

    async def chat_message(self, event):
        message = event["message"]
        username = event.get("username", "Unknown")
        await self.send(text_data=json.dumps({
            "message": message,
            "username": username
        }))


