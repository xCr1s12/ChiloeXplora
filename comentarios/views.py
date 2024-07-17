# views.py
from django.shortcuts import render, redirect
from .models import Comentario
from .forms import ComentarioForm
from django.contrib.auth.decorators import login_required

def mostrar_comentarios(request):
    comentarios = Comentario.objects.all().order_by('-fecha_creacion')
    form = ComentarioForm()
    return render(request, 'comentarios/comentarios.html', {'comentarios': comentarios, 'form': form})

@login_required
def agregar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.save()
            return redirect('mostrar_comentarios')
    return redirect('mostrar_comentarios')
