from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from chat_app.models import ChatGroup, ContactBook

User = get_user_model()


def get_last_messages(id):
    chatgroup = get_object_or_404(ChatGroup, id=id)
    return ChatGroup.group_messages.order_by('-timestamp').all()[:10]


def get_user_ContactBook_object(username):
    user = get_object_or_404(User, username=username)
    return get_object_or_404(ContactBook, user=user)


def get_current_ChatGroup(id):
    return get_object_or_404(ChatGroup, id)
