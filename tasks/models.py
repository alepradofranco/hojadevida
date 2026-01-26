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
    
class DatosPersonales(models.Model):
    perfil = models.OneToOneField(Perfil, related_name='datos_personales', on_delete=models.CASCADE)
    nacionalidad = models.CharField(max_length=50, blank=True)
    lugar_nacimiento = models.CharField(max_length=100, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    numero_cedula = models.CharField(max_length=20, blank=True)
    sexo = models.CharField(max_length=1, choices=[('H','Hombre'),('M','Mujer')], blank=True)
    estado_civil = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    sitio_web = models.URLField(blank=True)

    def __str__(self):
        return f"Datos de {self.perfil.user.username}"

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

class ExperienciaLaboral(models.Model):
    perfil = models.ForeignKey(Perfil, related_name='experiencias', on_delete=models.CASCADE)
    puesto = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.puesto} en {self.empresa}"
