from django.urls import path

from .views import report_reserva, inicio, ver_opcion_mantenimiento, backup, restore
urlpatterns = [
    path('reporte/reserva/', report_reserva, name='reporteReserva'),
    path('reporte/reserva/filrar/', inicio, name='filtrarReporteReserva'),
    path('reporte/mantenimiento/', ver_opcion_mantenimiento, name='mantenimiento'),
    path('reporte/mantenimiento/backup', backup, name='backup'),
    path('reporte/mantenimiento/restore', restore, name='restore'),
]
