from email import message
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def userchat(request):
    user = request.user
    return render(request, 'userchat.html', {'username': user.username, })