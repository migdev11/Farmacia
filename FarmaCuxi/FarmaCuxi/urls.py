"""
URL configuration for FarmaCuxi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path
from GesCuxi import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('sucursales/', views.lista_sucursales, name='lista_sucursales'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('medicamentos/', views.lista_medicamentos, name='lista_medicamentos'),
    path('inventario/', views.lista_inventario, name='lista_inventario'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('ventas/', views.lista_ventas, name='lista_ventas'),
    path('transferencias/', views.lista_transferencias, name='lista_transferencias'),
]