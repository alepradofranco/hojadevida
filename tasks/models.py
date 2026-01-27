from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ciudad = models.CharField(max_length=100, blank=True)
    pais = models.CharField(max_length=100, blank=True)
    biografia = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class DatosPersonales(models.Model):
    id = models.AutoField(primary_key=True)  # ID Perfil
    perfil = models.OneToOneField(Perfil, related_name='datos_personales', on_delete=models.CASCADE)
    descripcion_perfil = models.CharField(max_length=200, blank=True)  # Descripción del perfil
    perfil_activo = models.BooleanField(default=True)
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    lugar_nacimiento = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    numero_cedula = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1, choices=[('H', 'Hombre'), ('M', 'Mujer')])
    estado_civil = models.CharField(max_length=50)
    licencia_conducir = models.BooleanField(default=False)
    telefono_convencional = models.CharField(max_length=20, blank=True)
    telefono_fijo = models.CharField(max_length=20, blank=True)
    direccion_trabajo = models.CharField(max_length=200, blank=True)
    direccion_domiciliaria = models.CharField(max_length=200, blank=True)
    sitio_web = models.URLField(blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.nacionalidad}"


class ExperienciaLaboral(models.Model):
    id_experiencia = models.AutoField(primary_key=True)  # ID Experiencia Laboral
    perfil = models.ForeignKey(Perfil, related_name='experiencia_laboral', on_delete=models.CASCADE)
    cargo = models.CharField(max_length=200)  # Cargo desempeñado
    empresa = models.CharField(max_length=200)  # Nombre de la empresa
    lugar_empresa = models.CharField(max_length=200)  # Lugar de la empresa
    email_empresa = models.EmailField(blank=True)  # Email de la empresa
    sitio_web_empresa = models.URLField(blank=True)  # Sitio web de la empresa
    contacto_empresa = models.CharField(max_length=200, blank=True)  # Nombre del contacto empresarial
    telefono_contacto_empresa = models.CharField(max_length=20, blank=True)  # Teléfono del contacto empresarial
    fecha_inicio = models.DateField()  # Fecha inicio gestión
    fecha_fin = models.DateField(blank=True, null=True)  # Fecha fin gestión
    descripcion_funciones = models.TextField(blank=True)  # Descripción de funciones
    activo = models.BooleanField(default=True)  # Activar para que se vea en front
    certificado = models.URLField(blank=True)  # Ruta del certificado

    def __str__(self):
        return f"{self.empresa} - {self.cargo}"


class Reconocimientos(models.Model):
    id_reconocimiento = models.AutoField(primary_key=True)  # ID Reconocimiento
    perfil = models.ForeignKey(Perfil, related_name='reconocimientos', on_delete=models.CASCADE)
    tipo = models.CharField(
        max_length=50,
        choices=[('Académico', 'Académico'), ('Público', 'Público'), ('Privado', 'Privado')]
    )
    fecha = models.DateField()
    descripcion = models.TextField(blank=True)
    entidad = models.CharField(max_length=200)
    contacto = models.CharField(max_length=200, blank=True)
    telefono_contacto = models.CharField(max_length=20, blank=True)
    activo = models.BooleanField(default=True)
    certificado = models.URLField(blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.entidad}"


class CursosRealizados(models.Model):
    id_curso = models.AutoField(primary_key=True)  # ID Curso Realizado
    perfil = models.ForeignKey(Perfil, related_name='cursos_realizados', on_delete=models.CASCADE)
    nombre_curso = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    total_horas = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True)
    entidad = models.CharField(max_length=200)
    contacto = models.CharField(max_length=200, blank=True)
    telefono_contacto = models.CharField(max_length=20, blank=True)
    email_empresa = models.EmailField(blank=True)
    activo = models.BooleanField(default=True)
    certificado = models.URLField(blank=True)

    def __str__(self):
        return f"{self.nombre_curso} - {self.entidad}"


class ProductosAcademicos(models.Model):
    id_producto = models.AutoField(primary_key=True)  # ID Producto Académico
    perfil = models.ForeignKey(Perfil, related_name='productos_academicos', on_delete=models.CASCADE)
    nombre_recurso = models.CharField(max_length=200)
    clasificador = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_recurso} - {self.clasificador}"


class ProductosLaborales(models.Model):
    id_producto_laboral = models.AutoField(primary_key=True)  # ID Producto Laboral
    perfil = models.ForeignKey(Perfil, related_name='productos_laborales', on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=200)
    fecha_producto = models.DateField()
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_producto} - {self.fecha_producto}"


class VentaGarage(models.Model):
    id_venta_garage = models.AutoField(primary_key=True)  # ID Venta Garage
    perfil = models.ForeignKey(Perfil, related_name='venta_garage', on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=200)
    estado_producto = models.CharField(
        max_length=50,
        choices=[('Bueno', 'Bueno'), ('Regular', 'Regular')]
    )
    descripcion = models.TextField(blank=True)
    valor_bien = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_producto} - {self.estado_producto}"