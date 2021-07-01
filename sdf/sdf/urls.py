"""sdf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from sistemafinanzas.views import listar_creditos, ver_credito, aprobar_credito, desaprobar_credito

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar-creditos/', listar_creditos, name="listar-creditos"),
    path('ver-credito/<int>:credito_id', ver_credito, name="ver-credito"),
    path('aprobar-credito/<int>:credito_id', aprobar_credito, name="aprobar-credito"),
    path('desaprobar-credito/<int>:credito_id', desaprobar_credito, name="desaprobar-credito"),
]
