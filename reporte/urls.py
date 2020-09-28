from django.urls import path

from .views import report_reserva, generar_reporte, ver_opcion_mantenimiento, backup, restore
urlpatterns = [
    path('reporte/reserva/<str:fecha1>/<str:fecha2>/<str:estado>/', report_reserva),
    path('reporte/reserva/', report_reserva, name='reporteReserva'),
    path('reporte/reserva/filrar/', generar_reporte, name='filtrarReporteReserva'),
    path('reporte/mantenimiento/', ver_opcion_mantenimiento, name='mantenimiento'),
    path('reporte/mantenimiento/backup', backup, name='backup'),
    path('reporte/mantenimiento/restore', restore, name='restore'),
]
