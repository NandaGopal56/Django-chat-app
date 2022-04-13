from email import message
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Message, Room
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    return render(request, 'room/room.html', {'room': room, 'messages': messages})