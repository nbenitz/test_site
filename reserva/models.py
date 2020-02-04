from django.db import models
from estructura.models import Producto, Servicio, Habitacion
from persona.models import Cliente, Empleado
from django import forms
import datetime

# Create your models here.

def present_or_future_date(value):
    if value < datetime.date.today():
        raise forms.ValidationError("No se puede seleccionar una fecha pasada")
    return value

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    id_habitacion_fk = models.ForeignKey(Habitacion, 
                                       models.DO_NOTHING, 
                                       db_column='id_habitacion_fk',
                                       verbose_name="Habitaci&oacute;n")
    id_empleado_fk = models.ForeignKey(Empleado, 
                                       models.DO_NOTHING, 
                                       db_column='id_empleado_fk',
                                       verbose_name="Empleado",
                                       blank=True, 
                                       null=True)
    id_cliente_fk = models.ForeignKey(Cliente, 
                                      models.DO_NOTHING, 
                                      db_column='id_cliente_fk',
                                      verbose_name="Cliente")
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    costo_alojamiento = models.IntegerField()
    estado = models.CharField(max_length=10)

    class Meta:
        db_table = 'reserva'
        
    def __str__(self):      #Python 3
        return str(self.id_reserva)

class DetalleVentaProd(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    id_reserva_fk = models.ForeignKey('Reserva', 
                                      models.DO_NOTHING, 
                                      db_column='id_reserva_fk',
                                      verbose_name="Nro. Reserva")
    id_producto_fk = models.ForeignKey(Producto, 
                                       models.DO_NOTHING, 
                                       db_column='id_producto_fk',
                                       verbose_name="Producto")
    cantidad = models.FloatField()
    unidades = models.FloatField()
    precio = models.PositiveIntegerField(blank=True, null=True)
    obs = models.CharField(max_length=10)
    descuento = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'detalle_venta_prod'
        
        
class DetalleVentaServ(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    id_reserva_fk = models.ForeignKey('Reserva', 
                                      models.DO_NOTHING, 
                                      db_column='id_reserva_fk',
                                      verbose_name="Nro. Reserva")
    id_servicio_fk = models.ForeignKey(Servicio, 
                                       models.DO_NOTHING, 
                                       db_column='id_servicio_fk',
                                       verbose_name="Servicio")
    precio = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField()
    descuento = models.PositiveIntegerField()

    class Meta:
        db_table = 'detalle_venta_serv'


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_reserva = models.ForeignKey('Reserva', 
                                   models.DO_NOTHING, 
                                   db_column='id_reserva',
                                   verbose_name="Nro. Reserva")
    total_pago = models.PositiveIntegerField()
    fecha_pago = models.DateTimeField()

    class Meta:
        db_table = 'pago'
