"""
URL configuration for plataforma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.http import HttpResponse # Esto sirve para poder enviar strings a django.

def mi_func(xx): # Las funciones en url siempre reciben un argumento cuando hacemos funcionar el servidor.
    return HttpResponse("<h1>Bienvenidos a mi Proyecto!!!</h1>") # El HttpResponse se usa aquí para enviar strings.

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mi_func),
    path("bookings/", include("bookings.urls")) # Conectamos las URLS de "bookings" con las URLS generales. Necesitamos importar el "include".
]
