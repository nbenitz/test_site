#from django.shortcuts import render

# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
# Instanciamos los modelos para poder usarlo en nuestras Vistas CRUD
from .models import Habitacion, CategoriaHab

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
#from django import forms

# Create your views here.
#=================================== Habitacion ===========================================
class HabitacionListado(ListView): 
    model = Habitacion # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    #paginate_by = 10
    
class HabitacionCrear(SuccessMessageMixin, CreateView): 
    model = Habitacion # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = Habitacion # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Habitacion Creada Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerHabitacion') # Redireccionamos a la vista principal 'leer'
    
class HabitacionDetalle(DetailView): 
    model = Habitacion # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
 
class HabitacionActualizar(SuccessMessageMixin, UpdateView): 
    model = Habitacion # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = Habitacion # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Habitacion Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerHabitacion') # Redireccionamos a la vista principal 'leer'
   
class HabitacionEliminar(SuccessMessageMixin, DeleteView): 
    model = Habitacion 
    form = Habitacion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Habitacion Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerHabitacion') # Redireccionamos a la vista principal 'leer'

