from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from weasyprint import HTML
from .models import Perfil

def hoja_de_vida(request):
    perfil = Perfil.objects.first()  
    return render(request, 'hoja.html', {'perfil': perfil})

def descargar_cv(request):
    perfil = Perfil.objects.first()  
    template = get_template('hoja.html')  
    html_content = template.render({'perfil': perfil})

    pdf_file = HTML(string=html_content).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="hoja_de_vida.pdf"'
    return response