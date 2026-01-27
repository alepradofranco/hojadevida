from django.contrib import admin
from .models import (
    Perfil, DatosPersonales, Educacion, Experiencia,
    Reconocimiento, Curso, ProductoAcademico
)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'ciudad', 'pais', 'biografia')
    search_fields = ('user__username', 'ciudad', 'pais')

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'nacionalidad', 'lugar_nacimiento', 'fecha_nacimiento', 'numero_cedula', 'sexo', 'estado_civil', 'perfil_activo')
    list_filter = ('perfil_activo', 'sexo', 'estado_civil')
    search_fields = ('nacionalidad', 'numero_cedula')

@admin.register(Educacion)
class EducacionAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'titulo_obtenido', 'institucion', 'fecha_inicio', 'fecha_fin')
    list_filter = ('institucion',)
    search_fields = ('titulo_obtenido', 'institucion')

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'puesto', 'empresa', 'fecha_inicio', 'fecha_fin', 'activo')
    list_filter = ('activo', 'empresa')
    search_fields = ('puesto', 'empresa')

@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'tipo', 'entidad', 'fecha', 'activo')
    list_filter = ('activo', 'entidad')
    search_fields = ('tipo', 'entidad')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id_curso', 'perfil', 'nombre_curso', 'fecha_inicio', 'fecha_fin', 'total_horas', 'entidad', 'activo')
    list_filter = ('activo', 'entidad')
    search_fields = ('nombre_curso', 'entidad', 'contacto')

@admin.register(ProductoAcademico)
class ProductoAcademicoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'perfil', 'nombre_recurso', 'clasificador', 'activo')
    list_filter = ('activo', 'clasificador')
    search_fields = ('nombre_recurso', 'clasificador')