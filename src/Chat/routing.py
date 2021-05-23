from django.urls import path

from .consumers import ChatConsumer, ChatConsumer2

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
    path('ws/chat/etc/<str:room_name>/', ChatConsumer2.as_asgi()),
]
