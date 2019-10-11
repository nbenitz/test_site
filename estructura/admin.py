from django.contrib import admin

# Register your models here.
from .models import CategoriaHab, CategoriaProd, Proveedor, Producto, Servicio, Habitacion

class AdminProducto(admin.ModelAdmin):
    list_display = ["id_producto", "descripcion", "precio1", "stock"]
    #list_filter = ["id_producto", "descripcion"]
    search_fields = ["id_producto", "descripcion"]

class AdminHabitacion(admin.ModelAdmin):
    list_display = ["id_habitacion", "precio1", "numero", "id_categoria_fk", "caracteristicas", "estado"]
    #list_filter = ["id_habitacion", "numero"]
    search_fields = ["id_habitacion", "idhabitacion"]

admin.site.register(CategoriaHab)
admin.site.register(CategoriaProd)
admin.site.register(Proveedor)
admin.site.register(Producto, AdminProducto)
admin.site.register(Servicio)
admin.site.register(Habitacion, AdminHabitacion)


