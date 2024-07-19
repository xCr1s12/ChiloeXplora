from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UsuarioRegistroForm, UsuarioLoginForm
from django.urls import reverse
from core.supabase_client import supabase 
import bcrypt

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())

            # Crear el usuario en Supabase
            create_usuario(username, email, hashed_password)
            
            # Autenticar y loguear el usuario
            user_data = get_usuario_by_username(username)
            if user_data:
                user = authenticate(request, username=username, password=raw_password)
                if user:
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

            # Autenticar contra Supabase
            user_data = get_usuario_by_username(username)
            if user_data:
                stored_password = user_data[0]['password'].encode('utf-8')
                if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                    user = authenticate(request, username=username, password=password)
                    if user:
                        login(request, user)
                        return redirect(reverse('inicio'))
    else:
        form = UsuarioLoginForm()
    return render(request, 'Usuarios/iniciar_sesion.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect(reverse('inicio'))

# Funciones auxiliares
def create_usuario(username, email, hashed_password):
    data = {
        "username": username,
        "email": email,
        "password": hashed_password.decode('utf-8'),  # Guardar como string en la base de datos
    }
    response = supabase.table("usuarios").insert(data).execute()
    return response.data

def get_usuario_by_username(username):
    response = supabase.table("usuarios").select("*").eq("username", username).execute()
    return response.data
