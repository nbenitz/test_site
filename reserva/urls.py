# persona/urls.py
from django.urls import path

from .views import ReservaListado, ReservaDetalle, ReservaCrear, load_habitacion_disponible, ReservaAnular, ReservaAmpliar, \
                    DetalleVenta, ajax_search_products, ajax_add_product, ajax_modify_detalle_venta_prod, DetallePago

urlpatterns = [
    path('reserva/lista/<str:operacion>', ReservaListado.as_view(template_name = "reserva/index.html"), name='leerReserva'),
    path('reserva/detalle/<str:pk>/<str:operacion>', ReservaDetalle.as_view(template_name = "reserva/detalles.html"), name='detallesReserva'),
    path('reserva/crear', ReservaCrear.as_view(template_name = "reserva/crear.html"), name='crearReserva'),

    path('reserva/anular/<str:pk>', ReservaAnular.as_view(), name='anularReserva'),
    path('reserva/ampliar/<str:pk>', ReservaAmpliar.as_view(template_name = "reserva/ampliar.html"), name='ampliarReserva'),
    path('reserva/consumo/<str:pk>', DetalleVenta.as_view(template_name = "consumo/detalle_venta.html"), name='consumo'),
    path('reserva/detallepago/<str:pk>', DetallePago.as_view(template_name = "pago/detalle_pago.html"), name='detallePago'),

    #path('reserva/ajax/load-precio/', load_precio, name='ajax_load_precio'),

    #  ajax_calls
    path('ajax/search-products/<int:pk>/', ajax_search_products, name='ajax-search'),
    path('ajax/add-product/<int:pk>/<int:dk>/', ajax_add_product, name='ajax_add'),
    path('ajax/modify-product/<int:pk>/<slug:action>', ajax_modify_detalle_venta_prod, name='ajax_modify'),
    path('ajax/load-hab-disponible/', load_habitacion_disponible, name='ajax_load_hab_disponible'),

    #path('', views.index, name='index'),

]
