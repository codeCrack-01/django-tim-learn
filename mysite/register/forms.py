from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm (UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', "username", "email", 'password1', 'password2']
        widgets = {
            'last_name': forms.TextInput(attrs={'style': 'margin-bottom: 32px;'}),
        }