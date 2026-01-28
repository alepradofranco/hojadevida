from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Perfil

# Vista principal para mostrar la hoja de vida
def hoja_de_vida(request):
    perfil = Perfil.objects.first()
    if not perfil:
        return HttpResponse("No hay perfil registrado.", status=404)
    return render(request, 'hoja.html', {'perfil': perfil})

# Vista para descargar la hoja de vida en PDF
def descargar_cv(request):
    from weasyprint import HTML
    perfil = Perfil.objects.first()
    if not perfil:
        return HttpResponse("No hay perfil registrado.", status=404)
    template = get_template('hoja.html')
    html_content = template.render({'perfil': perfil})
    pdf_file = HTML(string=html_content).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="hoja_de_vida.pdf"'
    return response