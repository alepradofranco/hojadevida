#!/usr/bin/env bash
# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Recolectar archivos estáticos
python manage.py collectstatic --noinput

echo "from django.contrib.auth.models import User; \
User.objects.filter(username='pradoleyker').exists() or \
User.objects.create_superuser('pradoleyker', 'correo@ejemplo.com', 'Prado@2807')" \
| python manage.py shell