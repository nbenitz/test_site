# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CategoriaHab(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'categoria_hab'

    def __str__(self):  # Python 3
        return self.descripcion


class CategoriaProd(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'categoria_prod'
        
    def __str__(self):  # Python 3
        return self.descripcion

class Habitacion(models.Model):
    id_habitacion = models.AutoField(primary_key=True)
    precio1 = models.PositiveIntegerField(verbose_name="Precio")
    precio2 = models.PositiveIntegerField(blank=True, null=True)
    precio3 = models.PositiveIntegerField(blank=True, null=True)
    numero = models.IntegerField(unique=True, verbose_name="NÃºmero")
    id_categoria_fk = models.ForeignKey(CategoriaHab,
                                        models.DO_NOTHING,
                                        db_column='id_categoria_fk',
                                        verbose_name="Categor&iacute;a")
    caracteristicas = models.CharField(max_length=50,
                                       blank=True,
                                       null=True,
                                       verbose_name="Caracter&iacute;sticas")
    foto = models.ImageField(upload_to='hab-img', default='hab-img/no-foto.jpeg')
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'habitacion'
        
    def __str__(self):      #Python 3
        return str(self.numero)
            
        
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    ruc = models.CharField(unique=True, max_length=20)
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'proveedor'

    def __unicode__(self):  # Python 2
        return self.nombre

    def __str__(self):  # Python 3
        return self.nombre


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    barcode = models.CharField(unique=True, max_length=20)
    id_proveedor_fk = models.ForeignKey(Proveedor, 
                                        models.DO_NOTHING, 
                                        db_column='id_proveedor_fk',
                                        verbose_name="Proveedor")
    descripcion = models.CharField(max_length=50)
    id_categoria_fk = models.ForeignKey(CategoriaProd, 
                                        models.DO_NOTHING, 
                                        db_column='id_categoria_fk',
                                        verbose_name="Categor&iacute;a")
    costo = models.PositiveIntegerField()
    precio1 = models.PositiveIntegerField()
    precio2 = models.PositiveIntegerField(blank=True, null=True)
    precio3 = models.PositiveIntegerField(blank=True, null=True)
    stock = models.FloatField()
    presentacion = models.CharField(max_length=6,
                                    blank=True,
                                    null=True,
                                    verbose_name="Presentaci&oacute;n")
    foto = models.ImageField(upload_to='prod-img', default='prod-img/no-foto.jpeg')
    iva = models.PositiveIntegerField()
    precio_pack = models.PositiveIntegerField(blank=True, null=True)
    unid_x_pack = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'producto'

    def __unicode__(self):  # Python 2
        return self.descripcion

    def __str__(self):  # Python 3
        return self.descripcion


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'servicio'
        
    def __str__(self):      #Python 3
        return self.descripcion
    
    
class Dispositivo(models.Model):
    id_dispositivo = models.AutoField(primary_key=True)
    id_habitacion_fk = models.ForeignKey(Habitacion, 
                                        models.CASCADE, 
                                        db_column='id_habitacion_fk',
                                        verbose_name="Habitación")
    tipo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'dispositivo'
        
    def __str__(self):      #Python 3
        return self.descripcion

