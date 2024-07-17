from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    foto = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)

    def __str__(self):
        return self.username