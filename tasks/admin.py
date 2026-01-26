from django.contrib import admin
from .models import Perfil, DatosPersonales, Educacion, Lenguaje, Proyecto, ExperienciaLaboral, Reconocimiento

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'ciudad', 'pais', 'github')


@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'perfil_activo', 'nacionalidad', 'fecha_nacimiento', 'numero_cedula', 'licencia_conducir')
    list_filter = ('perfil_activo', 'licencia_conducir', 'sexo', 'estado_civil')


@admin.register(Educacion)
class EducacionAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'titulo_obtenido', 'institucion', 'fecha_inicio', 'fecha_fin')


@admin.register(Lenguaje)
class LenguajeAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'nombre', 'porcentaje_dominio')


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'nombre_proyecto', 'repositorio')


@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'puesto', 'empresa', 'activo')
    list_filter = ('activo',)


@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'tipo', 'fecha', 'entidad', 'activo')
    list_filter = ('tipo', 'activo')