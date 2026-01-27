from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ciudad = models.CharField(max_length=100, blank=True)
    pais = models.CharField(max_length=100, blank=True)
    biografia = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    def __str__(self): return self.user.username

class DatosPersonales(models.Model):
    perfil = models.OneToOneField(Perfil, related_name='datos_personales', on_delete=models.CASCADE)
    perfil_activo = models.BooleanField(default=True)
    nacionalidad = models.CharField(max_length=100)
    lugar_nacimiento = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    numero_cedula = models.CharField(max_length=20)
    sexo = models.CharField(max_length=20)
    estado_civil = models.CharField(max_length=50)
    licencia_conducir = models.BooleanField(default=False)
    telefono_convencional = models.CharField(max_length=20, blank=True)
    telefono_fijo = models.CharField(max_length=20, blank=True)
    direccion_trabajo = models.CharField(max_length=200, blank=True)
    direccion_domiciliaria = models.CharField(max_length=200, blank=True)
    sitio_web = models.URLField(blank=True)
    def __str__(self): return f"{self.perfil.user.username} - {self.nacionalidad}"

class Educacion(models.Model):
    perfil = models.ForeignKey(Perfil, related_name='educacion', on_delete=models.CASCADE)
    titulo_obtenido = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    def __str__(self): return f"{self.titulo_obtenido} - {self.institucion}"

class Experiencia(models.Model):
    perfil = models.ForeignKey(Perfil, related_name='experiencias', on_delete=models.CASCADE)
    puesto = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    lugar_empresa = models.CharField(max_length=200, blank=True)
    email_empresa = models.EmailField(blank=True)
    web_empresa = models.URLField(blank=True)
    contacto_empresa = models.CharField(max_length=200, blank=True)
    telefono_contacto = models.CharField(max_length=20, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    certificado = models.URLField(blank=True)
    def __str__(self): return f"{self.puesto} - {self.empresa}"

class Reconocimiento(models.Model):
    perfil = models.ForeignKey(Perfil, related_name='reconocimientos', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=200)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True)
    entidad = models.CharField(max_length=200, blank=True)
    contacto = models.CharField(max_length=200, blank=True)
    telefono_contacto = models.CharField(max_length=20, blank=True)
    activo = models.BooleanField(default=True)
    certificado = models.URLField(blank=True)
    def __str__(self): return f"{self.tipo} - {self.entidad}"

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    perfil = models.ForeignKey(Perfil, related_name='cursos', on_delete=models.CASCADE)
    nombre_curso = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    total_horas = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True)
    entidad = models.CharField(max_length=200, blank=True)
    contacto = models.CharField(max_length=200, blank=True)
    telefono_contacto = models.CharField(max_length=20, blank=True)
    email_empresa = models.EmailField(blank=True)
    activo = models.BooleanField(default=True)
    certificado = models.URLField(blank=True)
    def __str__(self): return f"{self.nombre_curso} - {self.entidad}"

class ProductoAcademico(models.Model):
    id_producto = models.AutoField(primary_key=True)
    perfil = models.ForeignKey(Perfil, related_name='productos_academicos', on_delete=models.CASCADE)
    nombre_recurso = models.CharField(max_length=200)
    clasificador = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    def __str__(self): return f"{self.nombre_recurso} - {self.clasificador}"