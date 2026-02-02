from django.contrib import admin
from django.urls import path, include, re_path # He añadido re_path aquí
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve # Lo movemos arriba por orden

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')), # <--- Asegúrate de que no tenga espacios: ''
]

# Configuración universal para archivos Media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # Esta es la parte mágica para Render
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]