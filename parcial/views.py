#from django.shortcuts import render

# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
# Instanciamos el modelo 'Empleado' y 'Persona' para poder usarlo en nuestras Vistas CRUD
from .models import Persona, Familia

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
from persona.models import Empleado
 
# Habilitamos los formularios en Django
#from django import forms

# Create your views here.

#=================================== Persona ===========================================
class PersonaListado(ListView): 
    model = Persona # Llamamos a la clase 'Persona' que se encuentra en nuestro archivo 'models.py'

    #paginate_by = 10
    
class PersonaCrear(SuccessMessageMixin, CreateView): 
    model = Persona # Llamamos a la clase 'Persona' que se encuentra en nuestro archivo 'models.py'
    form = Persona # Definimos nuestro formulario con el nombre de la clase o modelo 'Persona'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Persona' de nuestra Base de Datos 
    success_message = 'Persona Creada Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerPersona') # Redireccionamos a la vista principal 'leer'
    
class PersonaDetalle(DetailView): 
    model = Persona # Llamamos a la clase 'Persona' que se encuentra en nuestro archivo 'models.py'
 
class PersonaActualizar(SuccessMessageMixin, UpdateView): 
    model = Persona # Llamamos a la clase 'Persona' que se encuentra en nuestro archivo 'models.py' 
    form = Persona # Definimos nuestro formulario con el nombre de la clase o modelo 'Persona' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Persona' de nuestra Base de Datos 
    success_message = 'Persona Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerPersona') # Redireccionamos a la vista principal 'leer'
   
class PersonaEliminar(SuccessMessageMixin, DeleteView): 
    model = Persona 
    form = Persona
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Persona
    def get_success_url(self): 
        success_message = 'Persona Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Persona 
        messages.success (self.request, (success_message))       
        return reverse('leerPersona') # Redireccionamos a la vista principal 'leer'