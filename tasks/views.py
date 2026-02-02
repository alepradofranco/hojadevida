from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
import os
from .models import (
    Perfil, DatosPersonales, ExperienciaLaboral, Reconocimiento, 
    CursoRealizado, ProductoAcademico, ProductoLaboral, VentaGarage
)

# --- PÁGINAS PRINCIPALES ---

def home(request):
    perfil = Perfil.objects.filter(id=1).first() or Perfil.objects.first()
    datos_personales = None
    if perfil:
        datos_personales = DatosPersonales.objects.filter(perfil=perfil).first()
    return render(request, 'home.html', {'perfil': perfil, 'datos_personales': datos_personales})

def editar_perfil(request):
    return render(request, 'editar_perfil.html')

# --- LISTADOS DE SECCIONES (PÚBLICAS) ---

def experiencia(request):
    perfil_admin = Perfil.objects.filter(id=1).first() or Perfil.objects.first()
    experiencias_listado = ExperienciaLaboral.objects.filter(perfil=perfil_admin)
    return render(request, 'experiencia.html', {'experiencias': experiencias_listado, 'perfil': perfil_admin})

def cursos(request):
    perfil_admin = Perfil.objects.filter(id=1).first() or Perfil.objects.first()
    cursos_listado = CursoRealizado.objects.filter(perfil=perfil_admin)
    return render(request, 'cursos.html', {'cursos': cursos_listado, 'perfil': perfil_admin})

def reconocimientos(request):
    perfil_admin = Perfil.objects.filter(id=1).first() or Perfil.objects.first()
    reconocimientos_listado = Reconocimiento.objects.filter(perfil=perfil_admin)
    return render(request, 'reconocimientos.html', {'reconocimientos': reconocimientos_listado, 'perfil': perfil_admin})

def productos_academicos(request):
    perfil_admin = Perfil.objects.filter(id=1).first() or Perfil.objects.first()
    items = ProductoAcademico.objects.filter(perfil=perfil_admin)
    return render(request, 'productos_academicos.html', {'productos': items, 'perfil': perfil_admin})

def productos_laborales(request):
    perfil_admin = Perfil.objects.filter(id=1).first() or Perfil.objects.first()
    items = ProductoLaboral.objects.filter(perfil=perfil_admin)
    return render(request, 'productos_laborales.html', {'productos': items, 'perfil': perfil_admin})

def venta_garage(request):
    perfil_admin = Perfil.objects.filter(id=1).first() or Perfil.objects.first()
    items = VentaGarage.objects.filter(perfil=perfil_admin)
    return render(request, 'venta_garage.html', {'items': items, 'perfil': perfil_admin})

def garage(request):
    return render(request, 'garage.html')

# --- GENERACIÓN DE CV (PDF) ---

def seleccionar_apartados(request):
    return render(request, 'seleccionar_cv.html')

def descargar_cv(request):
    # Buscamos siempre al administrador (ID 1)
    perfil = Perfil.objects.filter(id=1).first() or Perfil.objects.first()
    if not perfil:
        return HttpResponse("No hay datos de perfil.", status=404)

    inc_exp = request.GET.get('experiencia') == 'on'
    inc_cur = request.GET.get('cursos') == 'on'
    inc_rec = request.GET.get('reconocimientos') == 'on'

    datos = DatosPersonales.objects.filter(perfil=perfil).first()
    
    # Aseguramos la URL absoluta para la imagen
    foto_url = None
    if perfil.foto:
        foto_url = request.build_absolute_uri(perfil.foto.url)

    context = {
        'perfil': perfil,
        'datos_personales': datos,
        'foto_url': foto_url,
        'incluir_experiencia': inc_exp,
        'experiencias': ExperienciaLaboral.objects.filter(perfil=perfil) if inc_exp else [],
        'incluir_cursos': inc_cur,
        'cursos': CursoRealizado.objects.filter(perfil=perfil) if inc_cur else [],
        'incluir_reconocimientos': inc_rec,
        'reconocimientos': Reconocimiento.objects.filter(perfil=perfil) if inc_rec else [],
    }

    template = get_template('cv_pdf_template.html')
    html_content = template.render(context)
    
    try:
        # Generamos el PDF usando la URL base de tu sitio
        pdf_file = HTML(string=html_content, base_url=request.build_absolute_uri('/')).write_pdf()
        response = HttpResponse(pdf_file, content_type='application/pdf')
        nombre_archivo = f"CV_{perfil.apellido if perfil.apellido else 'Admin'}.pdf"
        response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'
        return response
    except Exception as e:
        return HttpResponse(f"Error al generar el PDF: {e}", status=500)