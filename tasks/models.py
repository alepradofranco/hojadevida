from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        if hasattr(self, 'datos_personales'):
            return f"{self.datos_personales.nombres} {self.datos_personales.apellidos}"
        return self.user.username

class DatosPersonales(models.Model):
    SEXO_CHOICES = [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    ]

    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, related_name="datos_personales")
    descripcion_perfil = models.TextField(blank=True, null=True)
    perfil_activo = models.BooleanField(default=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    nombres = models.CharField(max_length=100, blank=True, null=True)
    nacionalidad = models.CharField(max_length=100, blank=True, null=True)
    lugar_nacimiento = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    numero_cedula = models.CharField(max_length=20, blank=True, null=True)
    sexo = models.CharField(max_length=20, blank=True, null=True)
    estado_civil = models.CharField(max_length=20, blank=True, null=True)
    licencia_conducir = models.BooleanField(default=False)
    telefono_convencional = models.CharField(max_length=20, blank=True, null=True)
    telefono_fijo = models.CharField(max_length=20, blank=True, null=True)
    direccion_trabajo = models.CharField(max_length=200, blank=True, null=True)
    direccion_domiciliaria = models.CharField(max_length=200, blank=True, null=True)
    sitio_web = models.URLField(blank=True, null=True)


class ExperienciaLaboral(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="experiencia_laboral")
    id_experiencia = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    lugar_empresa = models.CharField(max_length=100, blank=True, null=True)
    email_empresa = models.EmailField(blank=True, null=True)
    sitio_web_empresa = models.URLField(blank=True, null=True)
    contacto_empresa = models.CharField(max_length=100, blank=True, null=True)
    telefono_contacto_empresa = models.CharField(max_length=20, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    descripcion_funciones = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    certificado = models.URLField(blank=True, null=True)


class Reconocimiento(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="reconocimientos")
    id_reconocimiento = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.TextField()
    entidad = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    certificado = models.URLField(blank=True, null=True)


class CursoRealizado(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="cursos_realizados")
    id_curso = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    total_horas = models.IntegerField()
    descripcion = models.TextField()
    entidad = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    email_empresa = models.EmailField()
    activo = models.BooleanField(default=True)
    certificado = models.URLField(blank=True, null=True)


class ProductoAcademico(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="productos_academicos")
    id_producto = models.AutoField(primary_key=True)
    nombre_recurso = models.CharField(max_length=200)
    clasificador = models.CharField(max_length=100)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_recurso


class ProductoLaboral(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="productos_laborales")
    id_producto_laboral = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    fecha_producto = models.DateField()
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_producto


class VentaGarage(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="venta_garage")
    id_venta_garage = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    estado_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    valor_bien = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_producto