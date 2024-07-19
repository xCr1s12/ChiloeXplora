from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from .forms import ComentarioForm

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de Supabase
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Crea el cliente de Supabase
supabase: Client = create_client(url, key)

def mostrar_comentarios(request):
    # Consulta los comentarios desde Supabase
    comentarios_response = supabase.table('comentarios').select('*').order('fecha_creacion', desc=True).execute()
    comentarios = comentarios_response['data']
    
    form = ComentarioForm()
    return render(request, 'comentarios/comentarios.html', {'comentarios': comentarios, 'form': form})

@login_required
def agregar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario_data = {
                'contenido': comentario.contenido,
                'usuario': request.user.id,  # Asumiendo que quieres almacenar el ID del usuario
                'fecha_creacion': comentario.fecha_creacion
            }
            # Inserta el nuevo comentario en Supabase
            supabase.table('comentarios').insert(comentario_data).execute()
            return redirect('mostrar_comentarios')
    return redirect('mostrar_comentarios')
