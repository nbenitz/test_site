from django.contrib import admin

# Register your models here.
from .models import Cliente, Empleado


class AdminCliente(admin.ModelAdmin):
    list_display = ["id_cliente", "ci", "nombre", "telefono", "direccion"]
    # form = RegModelForm
    # list_display_links = ["nombre"]
    # list_filter = ["ci", "nombre", "telefono", "direccion"]
    # list_editable = ["nombre"]
    search_fields = ["ci", "nombre"]
    # class Meta:
    #    model = Registrado
    
class AdminEmpleado(admin.ModelAdmin):
    list_display = ["id_empleado", "ci", "nombre", "telefono", "direccion"]
    # form = RegModelForm
    # list_display_links = ["nombre"]
    # list_filter = ["ci", "nombre", "telefono", "direccion"]
    # list_editable = ["nombre"]
    search_fields = ["ci", "nombre"]
    # class Meta:
    #    model = Registrado


admin.site.register(Cliente, AdminCliente)
admin.site.register(Empleado)
