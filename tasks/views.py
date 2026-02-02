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


def home(request):
    # Intentamos buscar el perfil ID 1, si no existe, no rompemos la página
    perfil = Perfil.objects.filter(id=1).first() or Perfil.objects.first()
    datos_personales = None
    
    if perfil:
        datos_personales = DatosPersonales.objects.filter(perfil=perfil).first()
    
    context = {
        'perfil': perfil,
        'datos_personales': datos_personales,
    }
    return render(request, 'home.html', context)


def editar_perfil(request):
    # Lógica para renderizar el formulario de edición (asegúrate de tener editar_perfil.html)
    return render(request, 'editar_perfil.html')

# --- LISTADOS DE SECCIONES ---

def experiencia(request):
    # Buscamos siempre a tu perfil de Admin (ID 1)
    perfil_admin = Perfil.objects.filter(user__id=1).first() or Perfil.objects.first()
    
    # Traemos la experiencia laboral vinculada a ese perfil
    # .order_by('-fecha_inicio') opcional para mostrar lo más reciente primero
    experiencias_listado = ExperienciaLaboral.objects.filter(perfil=perfil_admin)
    
    return render(request, 'experiencia.html', {
        'experiencias': experiencias_listado,
        'perfil': perfil_admin
    })

def cursos(request):
    # Forzamos a buscar el perfil del usuario con ID 1 (Tu Admin)
    # Si por alguna razón el ID 1 no existe, trae el primero que encuentre
    perfil_admin = Perfil.objects.filter(user__id=1).first() or Perfil.objects.first()
    
    # Traemos todos los cursos asociados a ese perfil de administrador
    cursos_listado = CursoRealizado.objects.filter(perfil=perfil_admin)
    
    return render(request, 'cursos.html', {
        'cursos': cursos_listado,
        'perfil': perfil_admin
    })

def reconocimientos(request):
    # Buscamos siempre a tu usuario Admin (ID 1)
    perfil_admin = Perfil.objects.filter(user__id=1).first() or Perfil.objects.first()
    
    # Traemos los reconocimientos vinculados a ese perfil
    # Asegúrate de que el nombre del modelo sea 'Reconocimiento' o como lo hayas llamado
    reconocimientos_listado = Reconocimiento.objects.filter(perfil=perfil_admin)
    
    return render(request, 'reconocimientos.html', {
        'reconocimientos': reconocimientos_listado,
        'perfil': perfil_admin
    })


def productos_laborales(request):
    items = ProductoLaboral.objects.filter(perfil__user=request.user)
    return render(request, 'productos_laborales.html', {'productos': items})

def productos_academicos(request):
    # 1. Forzamos la búsqueda de tu perfil Admin (ID 1)
    # Esto asegura que los datos aparezcan aunque no estés logueado
    perfil_admin = Perfil.objects.filter(user__id=1).first() or Perfil.objects.first()
    
    # 2. Filtramos los productos académicos vinculados a ese perfil
    # Usamos 'productos' como nombre de variable para el context
    items = ProductoAcademico.objects.filter(perfil=perfil_admin)
    
    # 3. Renderizamos apuntando a la carpeta 'tasks/'
    return render(request, 'productos_academicos.html', {
        'productos': items, 
        'perfil': perfil_admin
    })


def garage(request):
    return render(request, 'garage.html')


def venta_garage(request):
    items = VentaGarage.objects.filter(perfil__user=request.user)
    return render(request, 'venta_garage.html', {'items': items})

# --- GENERACIÓN DE CV (PDF) ---


def seleccionar_apartados(request):
    return render(request, 'seleccionar_cv.html')


def descargar_cv(request):
    # Ya no usamos request.user porque es público. 
    # Buscamos directamente el perfil ID 1 (el tuyo).
    perfil = Perfil.objects.filter(id=1).first() or Perfil.objects.first()
    
    if not perfil:
        return HttpResponse("Error: No se encontró el perfil en la base de datos.", status=404)

    # Capturamos las opciones del formulario
    inc_exp = request.GET.get('experiencia') == 'on'
    inc_cur = request.GET.get('cursos') == 'on'
    inc_rec = request.GET.get('reconocimientos') == 'on'
    
    # IMPORTANTE: Datos personales suele ser una relación inversa
    datos_personales = DatosPersonales.objects.filter(perfil=perfil).first()

    context = {
        'perfil': perfil,
        'datos_personales': datos_personales,
        # Creamos la URL absoluta para la foto (Vital para Render/Cloudinary)
        'foto_url': request.build_absolute_uri(perfil.foto.url) if perfil.foto else None,
        
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
        # base_url es clave para que WeasyPrint encuentre archivos estáticos
        pdf_file = HTML(string=html_content, base_url=request.build_absolute_uri('/')).write_pdf()
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="CV_{perfil.nombre}.pdf"'
        return response
    except Exception as e:
        return HttpResponse(f"Error al generar el PDF: {e}", status=500)