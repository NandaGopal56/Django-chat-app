from curses.ascii import US
from dataclasses import fields
from statistics import mode
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1' , 'password2']
        