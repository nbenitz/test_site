from django import forms
from .models import Reserva
from django.forms.models import ModelForm
import datetime
from django.forms.widgets import Select, TextInput

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservaForm(ModelForm):
    #costo_alojamiento = forms.CharField(initial="50000")    
    class Meta:
        model = Reserva
        fields = ['id_cliente_fk', 'fecha_entrada', 'fecha_salida', 'id_habitacion_fk', 'costo_alojamiento']
        
        widgets = {
            #'id_cliente_fk': Select(attrs={'placeholder': 'Seleccionar Cliente'}),
            'fecha_entrada': DateInput(),
            'fecha_salida': DateInput(),
            #'id_habitacion_fk': Select(attrs={'onclick' : "return prueba();"}),
            #'costo_alojamiento': TextInput(attrs={'id' : "id_costo_alojamiento"}),
        }
        
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
    
    

