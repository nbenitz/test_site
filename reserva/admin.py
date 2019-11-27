from django.contrib import admin

from .models import Reserva, DetalleVentaProd, DetalleVentaServ, Pago

# Register your models here.
class AdminReserva(admin.ModelAdmin):
    list_display = ["id_reserva", "id_habitacion_fk", "fecha_reserva", "fecha_entrada", "fecha_salida"]

class AdminDetalleVentaProd(admin.ModelAdmin):
    list_display = ["id_detalle_venta", "id_producto_fk", "cantidad", "precio"]
    

admin.site.register(Reserva, AdminReserva)
admin.site.register(DetalleVentaProd, AdminDetalleVentaProd)
admin.site.register(DetalleVentaServ)
admin.site.register(Pago)