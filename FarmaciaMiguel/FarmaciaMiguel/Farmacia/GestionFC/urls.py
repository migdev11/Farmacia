from django.contrib import admin
from django.urls import path
from . import views  # Importamos la vista personalizada

urlpatterns = [
    path('', views.home, name='inicio'),  # Vista personalizada para la página de inicio
    path('admin/', admin.site.urls),    # Ruta del admin
]
