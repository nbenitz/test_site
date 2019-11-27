# persona/urls.py
from django.urls import path

from .views import ClienteListado, ClienteDetalle, ClienteCrear, ClienteActualizar, ClienteEliminar
from .views import EmpleadoListado, EmpleadoDetalle, EmpleadoCrear, EmpleadoActualizar, EmpleadoEliminar

urlpatterns = [
    path('cliente/', ClienteListado.as_view(template_name="cliente/index.html"), name='leerCliente'),
    path('cliente/detalle/<str:pk>', ClienteDetalle.as_view(template_name="cliente/detalles.html"), name='detallesCliente'),
    path('cliente/crear', ClienteCrear.as_view(template_name="cliente/crear.html"), name='crearCliente'),
    path('cliente/editar/<str:pk>', ClienteActualizar.as_view(template_name="cliente/actualizar.html"), name='actualizarCliente'),
    path('cliente/eliminar/<str:pk>', ClienteEliminar.as_view(), name='eliminarCliente'),

    path('empleado/', EmpleadoListado.as_view(template_name="empleado/index.html"), name='leerEmpleado'),
    path('empleado/detalle/<str:pk>', EmpleadoDetalle.as_view(template_name="empleado/detalles.html"), name='detallesEmpleado'),
    path('empleado/crear', EmpleadoCrear.as_view(template_name="empleado/crear.html"), name='crearEmpleado'),
    path('empleado/editar/<str:pk>', EmpleadoActualizar.as_view(template_name="empleado/actualizar.html"), name='actualizarEmpleado'),
    path('empleado/eliminar/<str:pk>', EmpleadoEliminar.as_view(), name='eliminarCliente'),
]
