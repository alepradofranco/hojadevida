from django.contrib import admin
from .models import (
    Perfil, DatosPersonales, ExperienciaLaboral, Reconocimientos,
    CursosRealizados, ProductosAcademicos, ProductosLaborales, VentaGarage
)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'ciudad', 'pais', 'biografia')
    search_fields = ('user__username', 'ciudad', 'pais')


@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'perfil', 'descripcion_perfil', 'perfil_activo',
        'apellidos', 'nombres', 'nacionalidad', 'lugar_nacimiento',
        'fecha_nacimiento', 'numero_cedula', 'sexo', 'estado_civil',
        'licencia_conducir', 'telefono_convencional', 'telefono_fijo',
        'direccion_trabajo', 'direccion_domiciliaria', 'sitio_web'
    )
    list_filter = ('perfil_activo', 'sexo', 'estado_civil')
    search_fields = ('apellidos', 'nombres', 'numero_cedula')


@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    list_display = (
        'id_experiencia', 'perfil', 'cargo', 'empresa', 'lugar_empresa',
        'email_empresa', 'sitio_web_empresa', 'contacto_empresa',
        'telefono_contacto_empresa', 'fecha_inicio', 'fecha_fin',
        'descripcion_funciones', 'activo', 'certificado'
    )
    list_filter = ('activo', 'empresa')
    search_fields = ('empresa', 'cargo', 'contacto_empresa')


@admin.register(Reconocimientos)
class ReconocimientosAdmin(admin.ModelAdmin):
    list_display = (
        'id_reconocimiento', 'perfil', 'tipo', 'fecha', 'descripcion',
        'entidad', 'contacto', 'telefono_contacto', 'activo', 'certificado'
    )
    list_filter = ('activo', 'tipo', 'entidad')
    search_fields = ('tipo', 'entidad', 'contacto')


@admin.register(CursosRealizados)
class CursosRealizadosAdmin(admin.ModelAdmin):
    list_display = (
        'id_curso', 'perfil', 'nombre_curso', 'fecha_inicio', 'fecha_fin',
        'total_horas', 'descripcion', 'entidad', 'contacto',
        'telefono_contacto', 'email_empresa', 'activo', 'certificado'
    )
    list_filter = ('activo', 'entidad')
    search_fields = ('nombre_curso', 'entidad', 'contacto')


@admin.register(ProductosAcademicos)
class ProductosAcademicosAdmin(admin.ModelAdmin):
    list_display = (
        'id_producto', 'perfil', 'nombre_recurso',
        'clasificador', 'descripcion', 'activo'
    )
    list_filter = ('activo', 'clasificador')
    search_fields = ('nombre_recurso', 'clasificador')


@admin.register(ProductosLaborales)
class ProductosLaboralesAdmin(admin.ModelAdmin):
    list_display = (
        'id_producto_laboral', 'perfil', 'nombre_producto',
        'fecha_producto', 'descripcion', 'activo'
    )
    list_filter = ('activo',)
    search_fields = ('nombre_producto', 'descripcion')


@admin.register(VentaGarage)
class VentaGarageAdmin(admin.ModelAdmin):
    list_display = (
        'id_venta_garage', 'perfil', 'nombre_producto',
        'estado_producto', 'descripcion', 'valor_bien', 'activo'
    )
    list_filter = ('estado_producto', 'activo')
    search_fields = ('nombre_producto', 'descripcion')