# persona/urls.py
from django.urls import path

from persona.views import ClienteListado, ClienteDetalle, activation_sent_view,\
    activate, activation_complete_view
from persona.views import EmpleadoListado, EmpleadoDetalle
from persona.views import UsuarioListado

from persona.views import create_client, edit_client, create_empleado, edit_empleado,\
    create_client2

urlpatterns = [
    path('cliente/', ClienteListado.as_view(template_name="cliente/index.html"), name='leerCliente'),
    path('cliente/detalle/<str:pk>', ClienteDetalle.as_view(template_name="cliente/detalles.html"), name='detallesCliente'),
    path('cliente/crear', create_client2, name='crearCliente'),
    path('cliente/editar/<str:pk>', edit_client, name='actualizarCliente'),
    #path('cliente/eliminar/<str:pk>', ClienteEliminar.as_view(), name='eliminarCliente'),

    path('empleado/', EmpleadoListado.as_view(template_name="empleado/index.html"), name='leerEmpleado'),
    path('empleado/detalle/<str:pk>', EmpleadoDetalle.as_view(template_name="empleado/detalles.html"), name='detallesEmpleado'),
    path('empleado/crear', create_empleado, name='crearEmpleado'),
    path('empleado/editar/<str:pk>', edit_empleado, name='actualizarEmpleado'),
    #path('empleado/eliminar/<str:pk>', EmpleadoEliminar.as_view(), name='eliminarEmpleado'),

    path('user/', UsuarioListado.as_view(template_name="user/index.html"), name='leerUsuario'),   
    #path('usuario/crear', WorkerCrear.as_view(template_name="usuario/crear.html"), name='crearUsuario'),
    #path('usuario/editar/<str:pk>', UsuarioActualizar.as_view(template_name="usuario/actualizar.html"), name='actualizarEmpleado'),

    path('signup/', create_client2, name="signup"),
    path('sent/', activation_sent_view, name="activation_send"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('activated/', activation_complete_view, name='activation_complete'),
    
]
