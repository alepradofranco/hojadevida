from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True)
    pais = models.CharField(max_length=100, blank=True)
    biografia = models.TextField(blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

class Educacion(models.Model):
    perfil = models.ForeignKey(Perfil, related_name='educacion', on_delete=models.CASCADE)
    titulo_obtenido = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)

class Lenguaje(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    porcentaje_dominio = models.PositiveIntegerField(default=0)

class Proyecto(models.Model):
    perfil = models.ForeignKey(Perfil, related_name='proyectos', on_delete=models.CASCADE)
    nombre_proyecto = models.CharField(max_length=200)
    descripcion_corta = models.TextField()
    repositorio = models.URLField(blank=True)
    imagen_destacada = models.ImageField(upload_to='proyectos/', blank=True, null=True)