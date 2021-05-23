from django.shortcuts import render


def index(request):
	return render(request, 'Chat/index.html', {})


def room(request, room_name):
	return render(request, 'Chat/chatroom.html', {'room_name': room_name})
