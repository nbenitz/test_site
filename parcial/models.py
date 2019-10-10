# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Familia(models.Model):
    id_familia = models.AutoField(primary_key=True)
    apellido = models.CharField(max_length=20)
    nro_cuenta = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20)

    class Meta:
        managed = False 
        db_table = 'familia'
        
    def __str__(self):      #Python 3
        return self.apellido + "\t@\t" + self.direccion


class Persona(models.Model):
    id_familia = models.ForeignKey(Familia, models.DO_NOTHING, db_column='id_familia', primary_key=True)
    nombre = models.CharField(unique=True, max_length=20)
    ci = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'persona'
        
    def __str__(self):      #Python 3
        return self.nombre
