from django.shortcuts import render
from reserva.models import Reserva
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse
from persona.models import Empleado
import json

from reserva.forms import ReservaForm
from django.http import HttpResponse
from estructura.models import Habitacion

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
    
def load_precio(request):
    id_habitacion = request.GET.get('habitacion')
    precio = Habitacion.objects.filter(id_habitacion=id_habitacion).values_list('precio1', flat=True)[0]
    #cities = City.objects.filter(country_id=country_id).order_by('name')
    #return render(request, 'hr/city_dropdown_list_options.html', {'cities': '135000'})
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
    lista_habitaciones = list(habitaciones.values('id_habitacion'))
    lista_hab_disponible = []
    
    for habitacion in lista_habitaciones:
        for id_habitacion in habitacion.keys():
            flag_habitacion_libre = True
            for hab_reservada in lista_hab_reservada:            
                for id_hab_reservada in hab_reservada.keys():
                    if hab_reservada[id_hab_reservada]==habitacion[id_habitacion]:
                        flag_habitacion_libre = False
                if flag_habitacion_libre == False:
                    print("Habitacion %s reservada" %(habitacion[id_habitacion]))
                    break
            if flag_habitacion_libre == True:
                print("Habitacion %s libre" %(habitacion[id_habitacion]))
                lista_hab_disponible.append({'habitacion': habitacion[id_habitacion]})
                
    JSONer = {}                
    JSONer['habitaciones'] = lista_hab_disponible
                        
    return HttpResponse(json.dumps(JSONer))

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
    
    
    
    