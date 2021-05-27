import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from chat_app.serializers import MessageSerializer
from chat_app.models import Message
from chat_app.utils import get_last_messages, get_user_ContactBook_object, get_current_ChatGroup


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        self.command[data['command']](self, data)

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message': message
        }))

    def send_message(self, content):
        self.send(text_data=json.dumps(content))

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def fetch_messages(self, data):
        messages = get_last_messages(data['chatId'])
        content = {
            'command': 'messages',
            'messages': self.serializer_meesages(messages)
        }
        self.send_message(content)

    def create_new_message(self, data):
        contact_book_object = get_user_ContactBook_object(data['user'])
        new_message = Message.objects.create(
            contact=contact_book_object,
            content=data['message']
        )
        chat_group = get_current_ChatGroup(data['id'])
        chat_group.messages.add(new_message)
        chat_group.save()

        content = {
            'command': 'new_message',
            'message': self.serializer_message(new_message)
        }
        return send_chat_group_message(self, content)

    def serializer_message(self, messages):
        result = []
        for message in messages:
            serializer = MessageSerializer(messages)
            result.append(serializer.data)

        print("result", result)
        return result

    command = {
        'fetch_messages': fetch_messages,
        'create_new_message': create_new_message
    }
