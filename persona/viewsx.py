# from django.shortcuts import render

# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model


# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render
from persona.forms import UserForm, ClienteForm

from django.http import HttpResponse

      
      
def index(request):
    return HttpResponse("MyClub Event Calendar")


 
# Habilitamos los formularios en Django
# from django import forms

# Create your views here.


#=================================== CLIENTE ===========================================
class ClienteListado(LoginRequiredMixin, ListView): 
    model = get_user_model()  # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py'
    
    def get_queryset(self):
        qs = self.model.objects.filter(is_client=1)
        return qs

def create_client_profile(request, pk):
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='UF')
        cliente_form = ClienteForm(request.POST, prefix='PF')
            
        if user_form.is_valid() and cliente_form.is_valid():
            user = user_form.save(commit=False)
            user_form.instance.is_client = True
            user.save()
    
            user.cliente.ci = cliente_form.cleaned_data.get('ci')
            user.cliente.save()
            messages.success(request, ('Perfil creado correctmente'))
            return redirect('leerCliente')
            
    else:
        user_form = UserForm(prefix='UF')
        cliente_form = ClienteForm(prefix='PF')
        
    return render(request, 'persona/cliente/crear.html',{
        'user_form': user_form,
        'cliente_form': cliente_form,
        })
    
class ClienteCrear(SuccessMessageMixin, CreateView): 
    model = get_user_model()  # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py'
    form = get_user_model()  # Definimos nuestro formulario con el nombre de la clase o modelo 'Cliente'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'cliente' de nuestra Base de Datos 
    success_message = 'Cliente Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerCliente')  # Redireccionamos a la vista principal 'leer'

    
class ClienteDetalle(DetailView): 
    model = get_user_model()  # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py'

 
class ClienteActualizar(SuccessMessageMixin, UpdateView): 
    model = get_user_model()  # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py' 
    form = get_user_model()  # Definimos nuestro formulario con el nombre de la clase o modelo 'Cliente' 
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'cliente' de nuestra Base de Datos 
    success_message = 'Cliente Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerCliente')  # Redireccionamos a la vista principal 'leer'

   
class ClienteEliminar(SuccessMessageMixin, DeleteView): 
    model = get_user_model() 
    form = get_user_model()
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o cliente
    def get_success_url(self): 
        success_message = 'Cliente Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Cliente 
        messages.success (self.request, (success_message))       
        return reverse('leerCliente')  # Redireccionamos a la vista principal 'leer'

#=================================== EMPLEADO ===========================================


class EmpleadoListado(ListView): 
    model = get_user_model() 

    
class EmpleadoCrear(SuccessMessageMixin, CreateView): 
    model = get_user_model()
    form = get_user_model()
    fields = "__all__"
    success_message = 'Empleado Creado Correctamente !'

    def get_success_url(self):
        return reverse('leerEmpleado')

    
class EmpleadoDetalle(DetailView): 
    model = get_user_model()

    
class EmpleadoActualizar(SuccessMessageMixin, UpdateView): 
    model = get_user_model()
    form = get_user_model()
    fields = "__all__" 
    success_message = 'Empleado Actualizado Correctamente !'
 
    def get_success_url(self):
        return reverse('leerEmpleado')


class EmpleadoEliminar(SuccessMessageMixin, DeleteView): 
    model = get_user_model() 
    form = get_user_model()
    fields = "__all__"
 
    def get_success_url(self): 
        success_message = 'Empleado Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leerEmpleado')
    
#=================================== USUARIO ===========================================
class UsuarioListado(ListView): 
    model = get_user_model() 
    


    


    
