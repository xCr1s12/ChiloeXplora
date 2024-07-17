# models.py
from django.db import models
from django.conf import settings

class Comentario(models.Model):
    contenido = models.TextField()
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.fecha_creacion}'
