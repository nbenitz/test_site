# persona/urls.py
from django.urls import path

from .views import ClienteListado, ClienteDetalle, ClienteCrear, ClienteActualizar, ClienteEliminar
from .views import EmpleadoListado

urlpatterns = [
    path('cliente', ClienteListado.as_view(template_name = "cliente/index.html"), name='leerCliente'),
    path('cliente/detalle/<str:pk>', ClienteDetalle.as_view(template_name = "cliente/detalles.html"), name='detalles'),
    path('cliente/crear', ClienteCrear.as_view(template_name = "cliente/crear.html"), name='crear'),
    path('cliente/editar/<str:pk>', ClienteActualizar.as_view(template_name = "cliente/actualizar.html"), name='actualizar'), 
    path('cliente/eliminar/<str:pk>', ClienteEliminar.as_view(), name='eliminar'),
    
    path('', EmpleadoListado.as_view(template_name = "empleado/index.html"), name='leerEmpleado'),
]
