from django.urls import path

from .views import report_reserva
urlpatterns = [
    path('reporte/reserva/', report_reserva, name='reporteReserva'),
]
