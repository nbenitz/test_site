# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class CategoriaHab(models.Model):
    idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoria_hab'
        
    def __unicode__(self):  #Python 2
        return self.descripcion
    
    def __str__(self):      #Python 3
        return self.descripcion

class CategoriaProd(models.Model):
    idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoria_prod'

class Habitacion(models.Model):
    idhabitacion = models.AutoField(db_column='idHabitacion', primary_key=True)  # Field name made lowercase.
    precio1 = models.PositiveIntegerField(db_column='Precio1')  # Field name made lowercase.
    precio2 = models.PositiveIntegerField(db_column='Precio2')  # Field name made lowercase.
    precio3 = models.PositiveIntegerField(db_column='Precio3')  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', unique=True)  # Field name made lowercase.
    idcategoriafk = models.ForeignKey(CategoriaHab, models.DO_NOTHING, db_column='idCategoriaFK')  # Field name made lowercase.
    caracteristicas = models.CharField(db_column='Caracteristicas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    foto = models.ImageField(db_column='Foto', blank=True, null=True, upload_to='photos')  # Field name made lowercase.
    estado = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'habitacion2'

class Proveedor(models.Model):
    ruc = models.CharField(db_column='RUC', primary_key=True, max_length=15)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=20)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=15, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proveedor'
        
    def __unicode__(self):  #Python 2
        return self.nombre
    
    def __str__(self):      #Python 3
        return self.nombre

class Producto(models.Model):
    idproducto = models.CharField(db_column='idProducto', primary_key=True, max_length=20)  # Field name made lowercase.
    idproveedorfk = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='idProveedorFK')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    costo = models.PositiveIntegerField(db_column='Costo')  # Field name made lowercase.
    precio1 = models.PositiveIntegerField(db_column='Precio1')  # Field name made lowercase.
    precio2 = models.PositiveIntegerField(db_column='Precio2')  # Field name made lowercase.
    precio3 = models.PositiveIntegerField(db_column='Precio3')  # Field name made lowercase.
    preciopack = models.PositiveIntegerField(db_column='PrecioPack', blank=True, null=True)  # Field name made lowercase.
    stock = models.FloatField(db_column='Stock')  # Field name made lowercase.
    unidxpack = models.FloatField(db_column='UnidXpack', blank=True, null=True)  # Field name made lowercase.
    porpack = models.CharField(db_column='PorPack', max_length=7, blank=True, null=True)  # Field name made lowercase.
    foto = models.TextField(db_column='Foto', blank=True, null=True)  # Field name made lowercase.
    iva = models.PositiveIntegerField(db_column='Iva')  # Field name made lowercase.
    lado1 = models.FloatField(db_column='Lado1', blank=True, null=True)  # Field name made lowercase.
    lado2 = models.FloatField(db_column='Lado2', blank=True, null=True)  # Field name made lowercase.
    categoria = models.ForeignKey(CategoriaProd, models.DO_NOTHING, db_column='Categoria')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto'
        
            
    def __unicode__(self):  #Python 2
        return self.descripcion
    
    def __str__(self):      #Python 3
        return self.descripcion

class Servicio(models.Model):
    idservicio = models.CharField(db_column='idServicio', primary_key=True, max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    precio = models.IntegerField(db_column='Precio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicio'

