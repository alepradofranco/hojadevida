from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('experiencia/', views.experiencia, name='experiencia'),
    path('cursos/', views.cursos, name='cursos'),
    path('reconocimientos/', views.reconocimientos, name='reconocimientos'),
    path('productos-laborales/', views.productos_laborales, name='productos_laborales'),
    path('productos-academicos/', views.productos_academicos, name='productos_academicos'),
    path('garage/', views.garage, name='garage'),
    path('ventagarage/', views.venta_garage, name='venta_garage'), # Esta línea ya no dará error
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('seleccionar-cv/', views.seleccionar_apartados, name='seleccionar_cv'),
    path('descargar-cv/', views.descargar_cv, name='descargar_cv'),
]