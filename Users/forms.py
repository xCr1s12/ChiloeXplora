from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class UsuarioRegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='')
    class Meta:
        model = Usuario
        fields = ('username','email', 'password1', 'password2')

class UsuarioLoginForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'password')
