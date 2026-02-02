#!/usr/bin/env bash
# exit on error
set -o errexit

# Actualizar pip e instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Crear superusuario si no existe (Tu código actual)
echo "from django.contrib.auth.models import User; \
User.objects.filter(username='pradoleyker').exists() or \
User.objects.create_superuser('pradoleyker', 'correo@ejemplo.com', 'Prado@2807')" \
| python manage.py shell