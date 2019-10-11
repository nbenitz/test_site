# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    ci = models.PositiveIntegerField(unique=True, max_length=15)
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cliente'

    def __unicode__(self):  #Python 2
        return self.nombre

    def __str__(self):      #Python 3
        return self.nombre

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    ci = models.PositiveIntegerField(unique=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField( max_length=20)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=30, blank=True, null=True)
    comision = models.PositiveIntegerField(blank=True, null=True)
    estado = models.CharField(max_length=8)

    class Meta:
        managed = True
        db_table = 'empleado'

    def __unicode__(self):  #Python 2
        return self.nombre

    def __str__(self):      #Python 3
        return self.nombre

class Privilegio(models.Model):
    id_privilegio = models.AutoField(primary_key=True)  # Field name made lowercase.
    rol = models.CharField(unique=True, max_length=20)  # Field name made lowercase.
    prod_consult = models.TextField()  # Field name made lowercase. This field type is a guess.
    prod_reg = models.TextField()  # Field name made lowercase. This field type is a guess.
    prod_actualiz = models.TextField()  # Field name made lowercase. This field type is a guess.
    prod_eliminar = models.TextField()  # Field name made lowercase. This field type is a guess.
    ventas_consult = models.TextField()  # Field name made lowercase. This field type is a guess.
    ventas_reg = models.TextField()  # Field name made lowercase. This field type is a guess.
    compras_consult = models.TextField()  # Field name made lowercase. This field type is a guess.
    compras_reg = models.TextField()  # Field name made lowercase. This field type is a guess.
    prov_consult = models.TextField()  # Field name made lowercase. This field type is a guess.
    prov_reg = models.TextField()  # Field name made lowercase. This field type is a guess.
    prov_actualiz = models.TextField()  # Field name made lowercase. This field type is a guess.
    prov_eliminar = models.TextField()  # Field name made lowercase. This field type is a guess.
    emple_admin = models.TextField()  # Field name made lowercase. This field type is a guess.
    usu_admin = models.TextField()  # Field name made lowercase. This field type is a guess.
    finanzas_admin = models.TextField()  # Field name made lowercase. This field type is a guess.
    hab_admin = models.TextField()  # Field name made lowercase. This field type is a guess.
    cuentas_admin = models.TextField()  # Field name made lowercase. This field type is a guess.
    devol_autori_cli = models.TextField()
    devol_autori_prov = models.TextField()

    class Meta:
        managed = False
        db_table = 'privilegio'

    def __unicode__(self):  #Python 2
        return self.rol

    def __str__(self):      #Python 3
        return self.rol

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(unique=True, max_length=20)  # Field name made lowercase.
    pass_field = models.CharField(max_length=20)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    id_privilegio_fk = models.ForeignKey(Privilegio, models.DO_NOTHING)  # Field name made lowercase.
    id_empleado_fk = models.ForeignKey(Empleado, models.DO_NOTHING, unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'

    def __unicode__(self):  #Python 2
        return self.usuario

    def __str__(self):      #Python 3
        return self.usuario
