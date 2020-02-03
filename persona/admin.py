from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from django.contrib.auth.models import User

# Register your models here.
from .models import User, Cliente, Empleado

    
# Define an inline admin descriptor for Worker model
# which acts a bit like a singleton
class ClientProfileInline(admin.StackedInline):
    model = Cliente
    can_delete = False
    verbose_name_plural = 'Clientes'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ClientProfileInline,)


admin.site.register(User, UserAdmin)
admin.site.register(Cliente)
admin.site.register(Empleado)