from django.contrib import admin
from .models import (
    Perfil, DatosPersonales, ExperienciaLaboral,
    Reconocimiento, CursoRealizado,
    ProductoAcademico, ProductoLaboral, VentaGarage
)

# Perfil
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'ciudad', 'pais', 'biografia')
    search_fields = ('user__username', 'ciudad', 'pais')
    list_filter = ('pais',)

# Datos Personales
@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información básica', {
            'fields': ('perfil', 'descripcion_perfil', 'perfil_activo')
        }),
        ('Identificación', {
            'fields': ('apellidos', 'nombres', 'nacionalidad', 'lugar_nacimiento',
                       'fecha_nacimiento', 'numero_cedula', 'sexo', 'estado_civil', 'licencia_conducir')
        }),
        ('Contacto', {
            'fields': ('telefono_convencional', 'telefono_fijo',
                       'direccion_trabajo', 'direccion_domiciliaria', 'sitio_web')
        }),
    )
    list_display = ('nombres', 'apellidos', 'nacionalidad', 'fecha_nacimiento', 'perfil_activo')
    search_fields = ('nombres', 'apellidos', 'nacionalidad')
    list_filter = ('perfil_activo',)

@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información laboral', {
            'fields': ('perfil', 'cargo', 'empresa', 'lugar_empresa',
                       'email_empresa', 'sitio_web_empresa')
        }),
        ('Contacto empresa', {
            'fields': ('contacto_empresa', 'telefono_contacto_empresa')
        }),
        ('Gestión', {
            'fields': ('fecha_inicio', 'fecha_fin', 'descripcion_funciones', 'activo', 'certificado', 'certificado_url')
        }),
    )
    list_display = ('cargo', 'empresa', 'fecha_inicio', 'fecha_fin', 'activo', 'certificado', 'certificado_url')
    search_fields = ('cargo', 'empresa')
    list_filter = ('activo',)

@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información', {
            'fields': ('perfil', 'tipo', 'fecha', 'descripcion', 'entidad')
        }),
        ('Contacto', {
            'fields': ('contacto', 'telefono_contacto')
        }),
        ('Estado', {
            'fields': ('activo', 'certificado', 'certificado_url')
        }),
    )
    list_display = ('tipo', 'entidad', 'fecha', 'activo', 'certificado', 'certificado_url')
    search_fields = ('tipo', 'entidad')
    list_filter = ('activo',)

@admin.register(CursoRealizado)
class CursoRealizadoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información curso', {
            'fields': ('perfil', 'nombre_curso', 'fecha_inicio', 'fecha_fin', 'total_horas', 'descripcion')
        }),
        ('Entidad', {
            'fields': ('entidad', 'contacto', 'telefono_contacto', 'email_empresa')
        }),
        ('Estado', {
            'fields': ('activo', 'certificado', 'certificado_url')
        }),
    )
    list_display = ('nombre_curso', 'entidad', 'fecha_inicio', 'fecha_fin', 'activo', 'certificado', 'certificado_url')
    search_fields = ('nombre_curso', 'entidad')
    list_filter = ('activo',)

# Productos Académicos
@admin.register(ProductoAcademico)
class ProductoAcademicoAdmin(admin.ModelAdmin):
    list_display = ('nombre_recurso', 'clasificador', 'activo')
    search_fields = ('nombre_recurso', 'clasificador')
    list_filter = ('activo',)

# Productos Laborales
@admin.register(ProductoLaboral)
class ProductoLaboralAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'fecha_producto', 'activo')
    search_fields = ('nombre_producto',)
    list_filter = ('activo',)

# Venta Garage
@admin.register(VentaGarage)
class VentaGarageAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'estado_producto', 'valor_bien', 'activo')
    search_fields = ('nombre_producto', 'estado_producto')
    list_filter = ('activo',)