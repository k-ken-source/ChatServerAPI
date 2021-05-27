from django.contrib import admin
from chat_app.models import Message, ContactBook, ChatGroup
# Register your models here.
admin.site.register(Message)
admin.site.register(ContactBook)
admin.site.register(ChatGroup)