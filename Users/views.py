from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UsuarioRegistroForm, UsuarioLoginForm
from django.urls import reverse

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect(reverse('inicio')) 
    else:
        form = UsuarioRegistroForm()
    return render(request, 'Usuarios/registro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = UsuarioLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('inicio'))
    else:
        form = UsuarioLoginForm()
    return render(request, 'Usuarios/iniciar_sesion.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect(reverse('inicio'))