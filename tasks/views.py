from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from .models import (
    Perfil, DatosPersonales, ExperienciaLaboral, Reconocimiento, 
    CursoRealizado, ProductoAcademico, ProductoLaboral, VentaGarage
)

# --- PÁGINAS PRINCIPALES ---

@login_required
def home(request):
    # Buscamos el perfil del usuario actual para mostrar su foto y descripción
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    # Buscamos sus datos personales (donde suele estar el nombre y contacto)
    datos_personales = DatosPersonales.objects.filter(perfil=perfil).first()
    
    context = {
        'perfil': perfil,
        'datos_personales': datos_personales,
    }
    return render(request, 'home.html', context)

@login_required
def editar_perfil(request):
    # Lógica para renderizar el formulario de edición (asegúrate de tener editar_perfil.html)
    return render(request, 'editar_perfil.html')

# --- LISTADOS DE SECCIONES ---

@login_required
def experiencia(request):
    items = ExperienciaLaboral.objects.filter(perfil__user=request.user)
    return render(request, 'experiencia.html', {'experiencias': items})

@login_required
def cursos(request):
    items = CursoRealizado.objects.filter(perfil__user=request.user)
    return render(request, 'cursos.html', {'cursos': items})

@login_required
def reconocimientos(request):
    items = Reconocimiento.objects.filter(perfil__user=request.user)
    return render(request, 'reconocimientos.html', {'reconocimientos': items})

@login_required
def productos_laborales(request):
    items = ProductoLaboral.objects.filter(perfil__user=request.user)
    return render(request, 'productos_laborales.html', {'productos': items})

@login_required
def productos_academicos(request):
    items = ProductoAcademico.objects.filter(perfil__user=request.user)
    return render(request, 'productos_academicos.html', {'productos': items})

@login_required
def garage(request):
    return render(request, 'garage.html')

@login_required
def venta_garage(request):
    items = VentaGarage.objects.filter(perfil__user=request.user)
    return render(request, 'venta_garage.html', {'items': items})

# --- GENERACIÓN DE CV (PDF) ---

@login_required
def seleccionar_apartados(request):
    return render(request, 'seleccionar_cv.html')

@login_required
def descargar_cv(request):
    perfil = get_object_or_404(Perfil, user=request.user)
    
    inc_exp = request.GET.get('experiencia') == 'on'
    inc_cur = request.GET.get('cursos') == 'on'
    inc_rec = request.GET.get('reconocimientos') == 'on'
    
    context = {
        'perfil': perfil,
        'datos_personales': getattr(perfil, 'datos_personales', None),
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
        pdf_file = HTML(string=html_content, base_url=request.build_absolute_uri('/')).write_pdf()
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="CV_{request.user.username}.pdf"'
        return response
    except Exception as e:
        return HttpResponse(f"Error al generar el PDF: {e}", status=500)