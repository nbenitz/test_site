# persona/urls.py
from django.urls import path
from django.contrib.auth import get_user_model

from persona.views import ObjetoListado, ObjetoDetalle, activation_sent_view,\
    activate, activation_complete_view
from persona.views import UsuarioListado

from persona.views import create_client, edit_client, create_empleado, edit_empleado,\
    create_client2

urlpatterns = [
    path('cliente/', ObjetoListado.as_view(template_name="cliente/index.html",
                                            model = get_user_model(),
                                            extra_context={'titulo':'Cliente',
                                                           'plural':'Clientes'}
                                            ), name='leerCliente', kwargs={'is_client':'1'}),
    
    path('cliente/detalle/<str:pk>', ObjetoDetalle.as_view(template_name="cliente/detalles.html",
                                                           model = get_user_model(),
                                                           extra_context={'titulo':'Cliente'}
                                                           ), name='detallesCliente'),
    
    path('cliente/crear', create_client2, name='crearCliente'),
    path('cliente/editar/<str:pk>', edit_client, name='actualizarCliente'),
    #path('cliente/eliminar/<str:pk>', ClienteEliminar.as_view(), name='eliminarCliente'),

    path('empleado/', ObjetoListado.as_view(template_name="empleado/index.html",
                                            model = get_user_model(),
                                            extra_context={'titulo':'Empleado',
                                                           'plural':'Empleados'}
                                            ), name='leerEmpleado', kwargs={'is_client':'0'}),
    
    path('empleado/detalle/<str:pk>', ObjetoDetalle.as_view(template_name="empleado/detalles.html",
                                                            model = get_user_model(),
                                                            extra_context={'titulo':'Empleado'}
                                                            ), name='detallesEmpleado'),
    
    path('empleado/crear', create_empleado, name='crearEmpleado'),
    path('empleado/editar/<str:pk>', edit_empleado, name='actualizarEmpleado'),
    #path('empleado/eliminar/<str:pk>', EmpleadoEliminar.as_view(), name='eliminarEmpleado'),

    path('user/', UsuarioListado.as_view(template_name="user/index.html"), name='leerUsuario'),   

    path('signup/', create_client2, name="signup"),
    path('sent/', activation_sent_view, name="activation_send"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('activated/', activation_complete_view, name='activation_complete'),
    
]

