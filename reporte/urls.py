from django.urls import path

from .views import report_reserva, inicio
urlpatterns = [
    path('reporte/reserva/', report_reserva, name='reporteReserva'),
    path('reporte/reserva/filrar/', inicio, name='filtrarReporteReserva'),
]
