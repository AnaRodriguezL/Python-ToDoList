"""
ASGI config for toDoList project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Establecer la variable de entorno que indica a Django que configuración usar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_list.settings')

# Obtener la aplicación ASGI que se pasa al servidor ASGI (por ejemplo, uvicorn)
application = get_asgi_application()

