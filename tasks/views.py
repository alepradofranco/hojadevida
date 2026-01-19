from django.shortcuts import render
from .models import Perfil

def hoja_de_vida(request):
    perfil = Perfil.objects.first()  # toma el primer perfil
    return render(request, 'hoja.html', {'perfil': perfil})