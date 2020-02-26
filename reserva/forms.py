from django import forms
from .models import Reserva, Pago
from django.forms.models import ModelForm
import datetime
from django.forms.widgets import Select, TextInput
from django.template.context_processors import request

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservaForm(ModelForm):
    #costo_alojamiento = forms.CharField(initial="50000")
    class Meta:
        model = Reserva
        fields = ['id_cliente_fk', 'fecha_entrada', 'fecha_salida', 'id_habitacion_fk', 'costo_alojamiento']
        """
        widgets = {
            'id_cliente_fk': Select(attrs={'placeholder': 'Seleccionar Cliente'}),
            'fecha_entrada': DateInput(),
            'fecha_salida': DateInput(),
            'id_habitacion_fk': TextInput(attrs={'placeholder': 'Seleccionar Habitación',
                                                 'readonly': 'true',
                                                 'style': 'background-color: white',
                                                 }),
            'id_habitacion_fk': Select(attrs={'placeholder' : "Seleccionar habitacion"}),
            'costo_alojamiento': TextInput(attrs={'readonly' : 'true'}),
        }"""
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')  # To get request.user. Do not use kwargs.pop('user', None) due to potential security hole
        super(ReservaForm, self).__init__(*args, **kwargs)
        if self.user.is_client:
            del self.fields['id_cliente_fk']
                
    def clean_fecha_entrada(self):
        fecha_entrada = self.cleaned_data['fecha_entrada']
        if fecha_entrada < datetime.date.today():
            raise forms.ValidationError("No se puede seleccionar una fecha pasada")
        return fecha_entrada   

    def clean_fecha_salida(self):
        fecha_salida = self.cleaned_data['fecha_salida']
        try:
            fecha_entrada = self.cleaned_data['fecha_entrada']
        except:
            fecha_entrada = datetime.date.today()
        if fecha_entrada:        
            if fecha_salida <= fecha_entrada:
                raise forms.ValidationError("La fecha de salida debe ser posterior a la fecha de entrada")
            return fecha_salida


class PagoForm(ModelForm):

    class Meta:
        model = Pago
        fields = ['total_pago']
        
    def __init__(self, *args, **kwargs):
        self.reserva = kwargs.pop('reserva') # se agrega 'reserva' como arg y se le asigna a la variable creada self.reserva
        super(PagoForm, self).__init__(*args, **kwargs)
        
    def clean_total_pago(self):
        reserva = self.reserva
        saldo_pendiente = Reserva.saldo_pendiente(reserva)
        total_pago = self.cleaned_data['total_pago']
        if total_pago > saldo_pendiente:
            raise forms.ValidationError("El monto a pagar no puede ser mayor al saldo pendiente")
        return total_pago 


