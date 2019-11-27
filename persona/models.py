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
    ci = models.CharField("C.I. Nro.", unique=True, max_length=15)
    nombre = models.CharField(max_length=30)
    telefono = models.CharField("Tel&eacute;fono", max_length=15, blank=True, null=True)
    direccion = models.CharField("Direcci&oacute;n", max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'cliente'

    def __unicode__(self):  # Python 2
        return self.nombre

    def __str__(self):  # Python 3
        return self.nombre


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    ci = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField("Tel&eacute;fono", max_length=15, blank=True, null=True)
    direccion = models.CharField("Direcci&oacute;n", max_length=50, blank=True, null=True)
    comision = models.PositiveIntegerField("Comisi&oacute;n", blank=True, null=True)
    estado = models.CharField(max_length=8)

    class Meta:
        db_table = 'empleado'

    def __unicode__(self):  # Python 2
        return self.nombre

    def __str__(self):  # Python 3
        return self.nombre

