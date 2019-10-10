# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Cliente(models.Model):
    ci = models.CharField(db_column='CI', primary_key=True, max_length=15)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=15, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
    #    managed = False
        db_table = 'cliente'
        
    #def __unicode__(self):  #Python 2
    #    return self.nombre
    
    #def __str__(self):      #Python 3
    #    return self.nombre

class Empleado(models.Model):
    ci = models.PositiveIntegerField(db_column='CI', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=20)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=20)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=15, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=30, blank=True, null=True)  # Field name made lowercase.
    comision = models.PositiveIntegerField(db_column='Comision', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleado'
        
    def __unicode__(self):  #Python 2
        return self.nombre
    
    def __str__(self):      #Python 3
        return self.nombre

class Privilegio(models.Model):
    idprivilegio = models.AutoField(db_column='idPrivilegio', primary_key=True)  # Field name made lowercase.
    rol = models.CharField(db_column='Rol', unique=True, max_length=20)  # Field name made lowercase.
    prodconsult = models.TextField(db_column='ProdConsult')  # Field name made lowercase. This field type is a guess.
    prodreg = models.TextField(db_column='ProdReg')  # Field name made lowercase. This field type is a guess.
    prodactualiz = models.TextField(db_column='ProdActualiz')  # Field name made lowercase. This field type is a guess.
    prodeliminar = models.TextField(db_column='ProdEliminar')  # Field name made lowercase. This field type is a guess.
    ventasconsult = models.TextField(db_column='VentasConsult')  # Field name made lowercase. This field type is a guess.
    ventasreg = models.TextField(db_column='VentasReg')  # Field name made lowercase. This field type is a guess.
    comprasconsult = models.TextField(db_column='ComprasConsult')  # Field name made lowercase. This field type is a guess.
    comprasreg = models.TextField(db_column='ComprasReg')  # Field name made lowercase. This field type is a guess.
    provconsult = models.TextField(db_column='ProvConsult')  # Field name made lowercase. This field type is a guess.
    provreg = models.TextField(db_column='ProvReg')  # Field name made lowercase. This field type is a guess.
    provactualiz = models.TextField(db_column='ProvActualiz')  # Field name made lowercase. This field type is a guess.
    proveliminar = models.TextField(db_column='ProvEliminar')  # Field name made lowercase. This field type is a guess.
    empleadmin = models.TextField(db_column='EmpleAdmin')  # Field name made lowercase. This field type is a guess.
    usuadmin = models.TextField(db_column='UsuAdmin')  # Field name made lowercase. This field type is a guess.
    finanzasadmin = models.TextField(db_column='FinanzasAdmin')  # Field name made lowercase. This field type is a guess.
    habadmin = models.TextField(db_column='HabAdmin')  # Field name made lowercase. This field type is a guess.
    cuentasadmin = models.TextField(db_column='CuentasAdmin')  # Field name made lowercase. This field type is a guess.
    devolautoricli = models.TextField(db_column='DevolAutoriCli')  # Field name made lowercase. This field type is a guess.
    devolautoriprov = models.TextField(db_column='DevolAutoriProv')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'privilegio'
        
    def __unicode__(self):  #Python 2
        return self.rol
    
    def __str__(self):      #Python 3
        return self.rol

class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', unique=True, max_length=20)  # Field name made lowercase.
    pass_field = models.CharField(db_column='Pass', max_length=20)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    idprivilegiofk = models.ForeignKey(Privilegio, models.DO_NOTHING, db_column='idPrivilegioFK')  # Field name made lowercase.
    idempleadofk = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='idEmpleadoFK', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
        
    def __unicode__(self):  #Python 2
        return self.usuario
    
    def __str__(self):      #Python 3
        return self.usuario
