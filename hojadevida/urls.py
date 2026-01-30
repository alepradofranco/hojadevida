from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # conecta todas las rutas de tu app "tasks"
]

# Para servir archivos multimedia (ej. fotos, certificados) en Render
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)