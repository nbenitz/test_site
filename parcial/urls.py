# estructura/urls.py
from django.urls import path

from .views import PersonaListado, PersonaDetalle, PersonaCrear, PersonaActualizar, PersonaEliminar

urlpatterns = [
    path('', PersonaListado.as_view(template_name = "persona/index.html"), name='leerPersona'),
    path('detalle/<str:pk>', PersonaDetalle.as_view(template_name = "persona/detalles.html"), name='detalles'),
    path('crear', PersonaCrear.as_view(template_name = "persona/crear.html"), name='crear'),
    path('editar/<str:pk>', PersonaActualizar.as_view(template_name = "persona/actualizar.html"), name='actualizar'), 
    path('eliminar/<str:pk>', PersonaEliminar.as_view(), name='eliminar'),
    
]
