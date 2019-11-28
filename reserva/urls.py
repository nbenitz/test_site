# persona/urls.py
from django.urls import path

from .views import ReservaListado, ReservaDetalle, ReservaCrear, ReservaActualizar, load_precio, load_habitacion_disponible

urlpatterns = [
    path('reserva/', ReservaListado.as_view(template_name = "reserva/index.html"), name='leerReserva'),
    path('reserva/detalle/<str:pk>', ReservaDetalle.as_view(template_name = "reserva/detalles.html"), name='detallesReserva'),
    path('reserva/crear', ReservaCrear.as_view(template_name = "reserva/crear.html"), name='crearReserva'),
    path('reserva/editar/<str:pk>', ReservaActualizar.as_view(template_name = "reserva/actualizar.html"), name='actualizarReserva'),

    path('reserva/ajax/load-precio/', load_precio, name='ajax_load_precio'),
    path('reserva/ajax/load-hab-disponible/', load_habitacion_disponible, name='ajax_load_hab_disponible'),
]
