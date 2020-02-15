# persona/urls.py
from django.urls import path

from .views import ReservaListado, ReservaDetalle, ReservaCrear, load_habitacion_disponible, ReservaAnular, ReservaAmpliar

urlpatterns = [
    path('reserva/lista/<str:operacion>', ReservaListado.as_view(template_name = "reserva/index.html"), name='leerReserva'),
    path('reserva/detalle/<str:pk>/<str:operacion>', ReservaDetalle.as_view(template_name = "reserva/detalles.html"), name='detallesReserva'),
    path('reserva/crear', ReservaCrear.as_view(template_name = "reserva/crear.html"), name='crearReserva'),

    path('reserva/anular/<str:pk>', ReservaAnular.as_view(), name='anularReserva'),
    path('reserva/ampliar/<str:pk>', ReservaAmpliar.as_view(template_name = "reserva/ampliar.html"), name='ampliarReserva'),
    

    #path('reserva/ajax/load-precio/', load_precio, name='ajax_load_precio'),
    path('reserva/ajax/load-hab-disponible/', load_habitacion_disponible, name='ajax_load_hab_disponible'),

    #path('', views.index, name='index'),

]
