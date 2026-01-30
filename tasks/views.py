from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from .models import Perfil

@login_required
def home(request):
    perfil = request.user.perfil
    return render(request, 'home.html', {'perfil': perfil})

@login_required
def experiencia(request):
    perfil = request.user.perfil
    return render(request, 'experiencia.html', {'perfil': perfil})

@login_required
def cursos(request):
    perfil = request.user.perfil
    return render(request, 'cursos.html', {'perfil': perfil})

@login_required
def reconocimientos(request):
    perfil = request.user.perfil
    return render(request, 'reconocimientos.html', {'perfil': perfil})

@login_required
def productos_laborales(request):
    perfil = request.user.perfil
    return render(request, 'productos_laborales.html', {'perfil': perfil})

@login_required
def productos_academicos(request):
    perfil = request.user.perfil
    return render(request, 'productos_academicos.html', {'perfil': perfil})

@login_required
def garage(request):
    perfil = request.user.perfil
    return render(request, 'garage.html', {'perfil': perfil})

@login_required
def venta_garage(request):
    perfil = request.user.perfil
    return render(request, 'ventagarage.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    perfil = request.user.perfil

    if request.method == 'POST':
        if 'avatar' in request.FILES:
            perfil.avatar = request.FILES['avatar']
        perfil.ciudad = request.POST.get('ciudad')
        perfil.pais = request.POST.get('pais')
        perfil.biografia = request.POST.get('biografia')
        perfil.save()
        return redirect('home')

    return render(request, 'perfil_form.html', {'perfil': perfil})

@login_required
def descargar_cv(request):
    perfil = request.user.perfil
    template = get_template('home.html')
    html_content = template.render({'perfil': perfil})

    # WeasyPrint convierte HTML a PDF respetando CSS moderno e imágenes
    pdf_file = HTML(string=html_content, base_url=request.build_absolute_uri()).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
    return response