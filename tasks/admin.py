from django.contrib import admin
from .models import (
    Perfil,
    DatosPersonales,
    ExperienciaLaboral,
    Reconocimiento,
    CursoRealizado,
    ProductoAcademico,
    ProductoLaboral,
    VentaGarage,
)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'nombres', 'apellidos', 'ciudad', 'pais')
    search_fields = ('nombres', 'apellidos', 'user__username', 'ciudad', 'pais')
    list_filter = ('pais', 'ciudad')
    fieldsets = (
        ('Datos de Usuario', {
            'fields': ('user', 'nombres', 'apellidos', 'biografia')
        }),
        ('Imagen de Perfil', {
            'fields': ('avatar',)
        }),
        ('Ubicación', {
            'fields': ('ciudad', 'pais')
        }),
    )

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'nombres', 'apellidos', 'nacionalidad', 'fecha_nacimiento', 'perfil_activo')
    search_fields = ('nombres', 'apellidos', 'nacionalidad', 'numero_cedula')
    list_filter = ('perfil_activo', 'nacionalidad', 'sexo', 'estado_civil')

@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'cargo', 'empresa', 'fecha_inicio', 'fecha_fin', 'activo')
    search_fields = ('cargo', 'empresa', 'contacto_empresa')
    list_filter = ('activo', 'empresa')

@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'tipo', 'entidad', 'fecha', 'activo')
    search_fields = ('tipo', 'entidad', 'contacto')
    list_filter = ('activo', 'fecha')

@admin.register(CursoRealizado)
class CursoRealizadoAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'nombre_curso', 'entidad', 'fecha_inicio', 'fecha_fin', 'activo')
    search_fields = ('nombre_curso', 'entidad', 'contacto')
    list_filter = ('activo', 'entidad')

@admin.register(ProductoAcademico)
class ProductoAcademicoAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'nombre_recurso', 'clasificador', 'activo')
    search_fields = ('nombre_recurso', 'clasificador')
    list_filter = ('activo',)

@admin.register(ProductoLaboral)
class ProductoLaboralAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'nombre_producto', 'fecha_producto', 'activo')
    search_fields = ('nombre_producto',)
    list_filter = ('activo', 'fecha_producto')

@admin.register(VentaGarage)
class VentaGarageAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'nombre_producto', 'estado_producto', 'valor_bien', 'activo')
    search_fields = ('nombre_producto', 'estado_producto')
    list_filter = ('activo',)