from django.contrib import admin
from .models import (
    Perfil, DatosPersonales, Reconocimientos,
    CursosRealizados, ProductosAcademicos
)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'ciudad', 'pais', 'biografia')
    search_fields = ('user__username', 'ciudad', 'pais')

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = (
        'perfil', 'perfil_activo', 'nacionalidad', 'lugar_nacimiento',
        'fecha_nacimiento', 'numero_cedula', 'sexo', 'estado_civil'
    )
    list_filter = ('perfil_activo', 'sexo', 'estado_civil')
    search_fields = ('nacionalidad', 'numero_cedula')

@admin.register(Reconocimientos)
class ReconocimientosAdmin(admin.ModelAdmin):
    list_display = (
        'perfil', 'tipo', 'fecha', 'entidad',
        'contacto', 'telefono_contacto', 'activo'
    )
    list_filter = ('activo', 'entidad')
    search_fields = ('tipo', 'entidad', 'contacto')

@admin.register(CursosRealizados)
class CursosRealizadosAdmin(admin.ModelAdmin):
    list_display = (
        'id_curso', 'perfil', 'nombre_curso', 'fecha_inicio',
        'fecha_fin', 'total_horas', 'entidad', 'activo'
    )
    list_filter = ('activo', 'entidad')
    search_fields = ('nombre_curso', 'entidad', 'contacto')

@admin.register(ProductosAcademicos)
class ProductosAcademicosAdmin(admin.ModelAdmin):
    list_display = (
        'id_producto', 'perfil', 'nombre_recurso',
        'clasificador', 'activo'
    )
    list_filter = ('activo', 'clasificador')
    search_fields = ('nombre_recurso', 'clasificador')