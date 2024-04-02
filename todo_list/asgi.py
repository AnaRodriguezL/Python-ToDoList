"""
ASGI config for toDoList project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Set the environment variable that tells Django which settings to use
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_list.settings')

# Get the ASGI application to pass to the ASGI server (e.g. uvicorn)
application = get_asgi_application()

