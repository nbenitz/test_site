from django.contrib import admin

# Register your models here.
from .models import Familia, Persona

class AdminPersona(admin.ModelAdmin):
    list_display = ["id_familia", "nombre", "ci"]
    #list_filter = ["idproducto", "descripcion"]
    search_fields = ["nombre"]
    
admin.site.register(Familia)
admin.site.register(Persona, AdminPersona)