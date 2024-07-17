# urls.py de la aplicación de comentarios
from django.urls import path
from . import views

app_name = 'comentarios'  # Añadir namespace a la aplicación de comentarios

urlpatterns = [
    path('', views.mostrar_comentarios, name='mostrar_comentarios'),
    path('agregar/', views.agregar_comentario, name='agregar_comentario'),
]
