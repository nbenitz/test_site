from django.shortcuts import render
from reserva.models import Reserva
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse
from persona.models import Empleado, Cliente
import json

from reserva.forms import ReservaForm
from django.http import HttpResponse
from estructura.models import Habitacion, CategoriaHab
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
#=================================== Reserva ===========================================
class ReservaCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    form_class = ReservaForm 
    success_message = 'Reserva Creada Correctamente !' 
    
    # Sending user object to the form, to verify which fields to display/remove (depending on group)
    def get_form_kwargs(self):
        kwargs = super(ReservaCrear, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
    
    def form_valid(self, form):
        if self.request.user.is_client:
            cliente = Cliente.objects.get(user_id=self.request.user.id)
            form.instance.id_cliente_fk = cliente
        else:            
            empleado = Empleado.objects.get(user_id=self.request.user.id)
            form.instance.id_empleado_fk = empleado
            
        return super().form_valid(form)
 
    def get_success_url(self):
        return reverse('leerReserva', args=['creado',])

    
def load_precio(request):
    id_habitacion = request.GET.get('habitacion')
    precio = Habitacion.objects.filter(id_habitacion=id_habitacion).values_list('precio1', flat=True)[0]
    return HttpResponse(precio)

def load_habitacion_disponible(request):
    entrada = request.GET.get('entrada')
    salida = request.GET.get('salida')
    
    habitaciones = Habitacion.objects.all()
    
    hab_reservada = Reserva.objects.filter(
        fecha_entrada__gte=entrada, 
        fecha_entrada__lt=salida
        )|Reserva.objects.filter(
            fecha_salida__gt=entrada, 
            fecha_salida__lte=salida
            )|Reserva.objects.filter(
                fecha_entrada__lte=entrada, 
                fecha_salida__gt=salida
                ).order_by('id_habitacion_fk')
                
    lista_hab_reservada = list(hab_reservada.values('id_habitacion_fk'))
    lista_habitaciones = list(habitaciones.values())
    lista_hab_disponible = []

    for habitacion in lista_habitaciones:
        flag_habitacion_libre = True
        for hab_reservada in lista_hab_reservada:            
            if hab_reservada['id_habitacion_fk'] == habitacion['id_habitacion']:
                flag_habitacion_libre = False
                print("Habitacion %s reservada" %(habitacion['id_habitacion']))
                break
        if flag_habitacion_libre == True:
            print("Habitacion %s libre" %(habitacion['id_habitacion']))
            categoria = CategoriaHab.objects.get(id_categoria=habitacion['id_categoria_fk_id'])
            lista_hab_disponible.append({'id': habitacion['id_habitacion'],
                                         'nro': habitacion['numero'],
                                         'categ': str(categoria),
                                         'carac': habitacion['caracteristicas'],
                                         'precio': habitacion['precio1'],
                                         'img': habitacion['foto'],
                                         })

                
    JSONer = {}                
    JSONer['habitaciones'] = lista_hab_disponible
                        
    return HttpResponse(json.dumps(JSONer))

class ReservaListado(LoginRequiredMixin, ListView): 
    model = Reserva
    #extra_context={'titulo': 'Anular Reserva'}
    
    def get_queryset(self):
        qs = self.model.objects.exclude(estado="Anulado")
        return qs    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["operacion"] = self.kwargs['operacion']
        return context
    
class ReservaDetalle(LoginRequiredMixin, DetailView): 
    model = Reserva
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["operacion"] = self.kwargs['operacion']
        return context
    
    
class ReservaAnular(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Reserva 
    form = Reserva 
    fields = []
    success_message = 'Reserva Anulada Correctamente !'
    
    def form_valid(self, form):
        form.instance.estado = "Anulado"
        return super().form_valid(form)
 
    def get_success_url(self):
        return reverse('leerReserva', args=['anular',])
    
class ReservaAmpliar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Reserva 
    form = Reserva 
    fields = ['fecha_entrada', 'fecha_salida', 'id_habitacion_fk', 'costo_alojamiento',]
    success_message = 'Reserva Ampliada Correctamente !' 
    
 
    def get_success_url(self):
        return reverse('leerReserva', args=['ampliar',])
    
    
    
    