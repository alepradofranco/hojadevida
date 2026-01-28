from django.contrib import admin
from .models import (
    Perfil, DatosPersonales, ExperienciaLaboral,
    Reconocimiento, CursoRealizado,
    ProductoAcademico, ProductoLaboral, VentaGarage
)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'ciudad', 'pais', 'biografia')
    search_fields = ('user__username', 'ciudad', 'pais')
    list_filter = ('pais',)

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'nacionalidad', 'fecha_nacimiento', 'perfil_activo')
    search_fields = ('nombres', 'apellidos', 'nacionalidad')
    list_filter = ('perfil_activo',)

@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'empresa', 'fecha_inicio', 'fecha_fin', 'activo')
    search_fields = ('cargo', 'empresa')
    list_filter = ('activo',)

@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'entidad', 'fecha', 'activo')
    search_fields = ('tipo', 'entidad')
    list_filter = ('activo',)

@admin.register(CursoRealizado)
class CursoRealizadoAdmin(admin.ModelAdmin):
    list_display = ('nombre_curso', 'entidad', 'fecha_inicio', 'fecha_fin', 'activo')
    search_fields = ('nombre_curso', 'entidad')
    list_filter = ('activo',)

@admin.register(ProductoAcademico)
class ProductoAcademicoAdmin(admin.ModelAdmin):
    list_display = ('nombre_recurso', 'clasificador', 'activo')
    search_fields = ('nombre_recurso', 'clasificador')
    list_filter = ('activo',)

@admin.register(ProductoLaboral)
class ProductoLaboralAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'fecha_producto', 'activo')
    search_fields = ('nombre_producto',)
    list_filter = ('activo',)

@admin.register(VentaGarage)
class VentaGarageAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'estado_producto', 'valor_bien', 'activo')
    search_fields = ('nombre_producto', 'estado_producto')
    list_filter = ('activo',)