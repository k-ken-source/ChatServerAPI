from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from chat_app.models import ChatGroup
from chat_app.serializers import ChatGroupSerializer


class ChatGroupListCreateView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChatGroupSerializer
    queryset = ChatGroup.objects.all()


class ChatGroupRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChatGroupSerializer
    queryset = ChatGroup.objects.all()
