from django.shortcuts import render
from reserva.models import Reserva
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse
from persona.models import Empleado

from reserva.forms import ReservaForm

# Create your views here.
#=================================== Reserva ===========================================
class ReservaCrear(SuccessMessageMixin, CreateView): 
    form_class = ReservaForm 
    success_message = 'Reserva Creada Correctamente !' 
    
    def form_valid(self, form):
        empleado = Empleado.objects.get(id_empleado=1)        
        form.instance.id_empleado_fk = empleado
        form.instance.costo_alojamiento = "50000"
        return super().form_valid(form)    
 
    def get_success_url(self):        
        return reverse('leerReserva')

class ReservaListado(ListView): 
    model = Reserva
    
class ReservaDetalle(DetailView): 
    model = Reserva
 
class ReservaActualizar(SuccessMessageMixin, UpdateView): 
    model = Reserva 
    form = Reserva 
    fields = "__all__" 
    success_message = 'Reserva Actualizada Correctamente !'
 
    def get_success_url(self):               
        return reverse('leerReserva')
    
    
    
    