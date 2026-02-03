from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('experiencia/', views.experiencia, name='experiencia'),
    path('cursos/', views.cursos, name='cursos'),
    path('reconocimientos/', views.reconocimientos, name='reconocimientos'),
    path('productos-laborales/', views.productos_laborales, name='productos_laborales'),
    path('productos-academicos/', views.productos_academicos, name='productos_academicos'),
    
    # SOLO DEJA ESTA LÍNEA PARA EL GARAGE:
    path('garage/', views.venta_garage, name='garage'), 
    
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('seleccionar-cv/', views.seleccionar_apartados, name='seleccionar_cv'),
    path('descargar-cv/', views.descargar_cv, name='descargar_cv'),
]