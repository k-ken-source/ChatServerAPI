from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactBook(models.Model):
    user = models.ForeignKey(User, related_name='contact_user', on_delete=models.CASCADE)
    contact_list = models.ManyToManyField('self', blank=True, symmetrical=True)


class Message(models.Model):
    contact = models.ForeignKey(ContactBook, blank=False, related_name="contact", on_delete=models.DO_NOTHING)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact.user.username

    def get_last_messages(self, n):
        Message.objects.order_by('-timestamp').all()[:n]


class ChatGroup(models.Model):
    participants = models.ManyToManyField(ContactBook, related_name='chat_group_participants', blank=True)
    messages = models.ManyToManyField(Message, related_name='group_messages', blank=True)
