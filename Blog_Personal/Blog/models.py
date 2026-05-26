from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='perfiles/', null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"

class Post(models.Model):
    # foreignKey con el user
    titulo = models.CharField(max_length=200)
    asunto = models.CharField(max_length=300)
    contenido = models.TextField()
    foto = models.ImageField(upload_to='posts/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo