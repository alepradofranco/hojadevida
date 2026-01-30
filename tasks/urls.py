from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('experiencia/', views.experiencia, name='experiencia'),
    path('cursos/', views.cursos, name='cursos'),
    path('reconocimientos/', views.reconocimientos, name='reconocimientos'),
    path('productos_laborales/', views.productos_laborales, name='productos_laborales'),
    path('productos_academicos/', views.productos_academicos, name='productos_academicos'),
    path('garage/', views.garage, name='garage'),
    path('ventagarage/', views.venta_garage, name='venta_garage'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('descargar_cv/', views.descargar_cv, name='descargar_cv'),
]