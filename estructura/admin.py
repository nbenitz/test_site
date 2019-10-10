from django.contrib import admin

# Register your models here.
from .models import CategoriaHab, CategoriaProd, Proveedor, Producto, Servicio, Habitacion

class AdminProducto(admin.ModelAdmin):
    list_display = ["idproducto", "descripcion", "precio1", "stock"]
    list_filter = ["idproducto", "descripcion"]
    search_fields = ["idproducto", "descripcion"]
    
class AdminHabitacion(admin.ModelAdmin):
    list_display = ["idhabitacion", "precio1", "numero", "idcategoriafk", "caracteristicas", "estado"]
    list_filter = ["idhabitacion", "numero"]
    search_fields = ["idhabitacion", "idhabitacion"]

admin.site.register(CategoriaHab)
admin.site.register(CategoriaProd)
admin.site.register(Proveedor)
admin.site.register(Producto, AdminProducto)
admin.site.register(Servicio)
admin.site.register(Habitacion, AdminHabitacion)


