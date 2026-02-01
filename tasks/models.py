from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Perfil principal
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Datos básicos
    nombres = models.CharField(max_length=100, blank=True)
    apellidos = models.CharField(max_length=100, blank=True)
    biografia = models.TextField(blank=True)

    # Imagen de perfil
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    # Ubicación
    ciudad = models.CharField(max_length=100, blank=True)
    pais = models.CharField(max_length=100, blank=True)

    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}".strip()

    def __str__(self):
        return self.nombre_completo() or self.user.username


# Señales para crear y guardar Perfil automáticamente
@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    try:
        instance.perfil.save()
    except Perfil.DoesNotExist:
        pass


# Datos personales extendidos
class DatosPersonales(models.Model):
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


# Experiencia laboral
class ExperienciaLaboral(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="experiencia_laboral")
    cargo = models.CharField(max_length=100, blank=True, null=True)
    empresa = models.CharField(max_length=100, blank=True, null=True)
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
    certificado_archivo = models.FileField(upload_to='certificados/', blank=True, null=True)


# Reconocimientos
class Reconocimiento(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="reconocimientos")
    tipo = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    entidad = models.CharField(max_length=100, blank=True, null=True)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    telefono_contacto = models.CharField(max_length=20, blank=True, null=True)
    activo = models.BooleanField(default=True)
    certificado = models.URLField(blank=True, null=True)
    certificado_archivo = models.FileField(upload_to='certificados/', blank=True, null=True)


# Cursos realizados
class CursoRealizado(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="cursos_realizados")
    nombre_curso = models.CharField(max_length=200, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    total_horas = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    entidad = models.CharField(max_length=100, blank=True, null=True)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    telefono_contacto = models.CharField(max_length=20, blank=True, null=True)
    email_empresa = models.EmailField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    certificado = models.URLField(blank=True, null=True)
    certificado_archivo = models.FileField(upload_to='certificados/', blank=True, null=True)


# Productos académicos
class ProductoAcademico(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="productos_academicos")
    nombre_recurso = models.CharField(max_length=200, blank=True, null=True)
    clasificador = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_recurso or ""


# Productos laborales
class ProductoLaboral(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="productos_laborales")
    nombre_producto = models.CharField(max_length=200, blank=True, null=True)
    fecha_producto = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_producto or ""


# Venta garage
class VentaGarage(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="venta_garage")
    nombre_producto = models.CharField(max_length=200, blank=True, null=True)
    estado_producto = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    valor_bien = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_producto or ""