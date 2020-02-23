from django.db import models
from estructura.models import Producto, Servicio, Habitacion
from persona.models import Cliente, Empleado
from django import forms
import datetime
from django.conf import settings
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_delete
from django.db.models import Sum, F, DecimalField
from django.contrib.humanize.templatetags.humanize import intcomma

CURRENCY = settings.CURRENCY

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
        
    def __str__(self):
        return str(self.id_reserva)
    
    def tag_costo_alojamiento(self):
        return f'{intcomma(self.costo_alojamiento)} {CURRENCY}'
    
    def total_consumo(self):
        detalle_venta_prod = self.detalle_venta_prod.all()
        total_consumo = detalle_venta_prod.aggregate(
            sub_total=Sum(F('precio')*F('cantidad'), output_field=DecimalField())
            )['sub_total'] if detalle_venta_prod.exists() else 0
        print(total_consumo)
        return total_consumo
    
    def tag_total_consumo(self):
        return f'{intcomma(self.total_consumo())} {CURRENCY}'
    
    def tag_total(self):
        total = self.costo_alojamiento + self.total_consumo()
        return f'{intcomma(total)} {CURRENCY}'

class DetalleVentaProd(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    id_reserva_fk = models.ForeignKey('Reserva', 
                                      models.DO_NOTHING, 
                                      db_column='id_reserva_fk',
                                      verbose_name="Nro. Reserva",
                                      related_name='detalle_venta_prod')
    id_producto_fk = models.ForeignKey(Producto, 
                                       models.DO_NOTHING, 
                                       db_column='id_producto_fk',
                                       verbose_name="Producto")
    cantidad = models.FloatField(default=1)
    unidades = models.FloatField(default=1)
    precio = models.PositiveIntegerField(default=0)
    obs = models.CharField(max_length=10, blank=True, null=True)
    descuento = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'detalle_venta_prod'
        
    def tag_precio(self):
        return intcomma(self.precio)
    
    def tag_cantidad(self):
        return intcomma(int(self.cantidad))
    
    def tag_sub_total(self):
        sub_total = int(self.cantidad) * self.precio
        return intcomma(sub_total)
    
@receiver(post_delete, sender=DetalleVentaProd)
def delete_detalle_venta_prod(sender, instance, **kwargs):
    product = instance.id_producto_fk
    product.stock += instance.cantidad
    product.save()
    instance.id_reserva_fk.save()
        
        
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
