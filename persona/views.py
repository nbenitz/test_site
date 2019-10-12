#from django.shortcuts import render

# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
# Instanciamos el modelo 'Empleado' y 'Cliente' para poder usarlo en nuestras Vistas CRUD
from .models import Empleado, Cliente

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
#from django import forms

# Create your views here.

#=================================== CLIENTE ===========================================
class ClienteListado(ListView): 
    model = Cliente # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py'
    #paginate_by = 10
    
class ClienteCrear(SuccessMessageMixin, CreateView): 
    model = Cliente # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py'
    form = Cliente # Definimos nuestro formulario con el nombre de la clase o modelo 'Cliente'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'cliente' de nuestra Base de Datos 
    success_message = 'Cliente Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerCliente') # Redireccionamos a la vista principal 'leer'

    
class ClienteDetalle(DetailView): 
    model = Cliente # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py'
 
class ClienteActualizar(SuccessMessageMixin, UpdateView): 
    model = Cliente # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py' 
    form = Cliente # Definimos nuestro formulario con el nombre de la clase o modelo 'Cliente' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'cliente' de nuestra Base de Datos 
    success_message = 'Cliente Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerCliente') # Redireccionamos a la vista principal 'leer'
   
class ClienteEliminar(SuccessMessageMixin, DeleteView): 
    model = Cliente 
    form = Cliente
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o cliente
    def get_success_url(self): 
        success_message = 'Cliente Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Cliente 
        messages.success (self.request, (success_message))       
        return reverse('leerCliente') # Redireccionamos a la vista principal 'leer'

#=================================== EMPLEADO ===========================================

class EmpleadoListado(ListView): 
    model = Empleado 
    
class EmpleadoCrear(SuccessMessageMixin, CreateView): 
    model = Empleado
    form = Empleado
    fields = "__all__"
    success_message = 'Empleado Creado Correctamente !'

    def get_success_url(self):
        return reverse('leer')
    
class EmpleadoDetalle(DetailView): 
    model = Empleado
    
class EmpleadoActualizar(SuccessMessageMixin, UpdateView): 
    model = Empleado
    form = Empleado
    fields = "__all__" 
    success_message = 'Cliente Actualizado Correctamente !'
 
    def get_success_url(self):
        return reverse('leer')

class EmpleadoEliminar(SuccessMessageMixin, DeleteView): 
    model = Empleado 
    form = Empleado
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Empleado Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leer')
    