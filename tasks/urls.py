from django.urls import path
from . import views

urlpatterns = [
    path('', views.hoja_de_vida, name='hoja'),
    path('descargar-cv/', views.descargar_cv, name='descargar_cv'),
]