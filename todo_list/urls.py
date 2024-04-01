from django.contrib import admin
from django.urls import path, include

# Esta es la configuración de URLs para la aplicación todo_list.
# La lista `urlpatterns` enrutan URLs a vistas. Para más información, por favor visite:
# https://docs.djangoproject.com/en/5.0/topics/http/urls/

# Ejemplos:
#     Vistas basadas en funciones
#     1. Agregue una importación:  from mi_app import views
#     2. Agregue una URL a urlpatterns:  path('', views.home, name='home')

#     Vistas basadas en clases
#     1. Agregue una importación:  from otra_app.views import Home
#     2. Agregue una URL a urlpatterns:  path('', Home.as_view(), name='home')

# Incluyendo otra URLconf
#     1. Importe la función include():  from django.urls import include, path
#     2. Agregue una URL a urlpatterns:  path('blog/', include('blog.urls'))

urlpatterns = [
    # URL a la página de administración.
    path('admin/', admin.site.urls),

    # Incluye las URLs de la aplicación de tareas.
    path('', include('todo.urls')),
]
