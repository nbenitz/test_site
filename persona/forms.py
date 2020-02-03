from django import forms
from .models import Cliente, Empleado
from django.forms.models import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


        
class UserForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'telefono', 'direccion')
        
        widgets = {
            'password': forms.PasswordInput(),
        }

class ClienteForm(ModelForm):
    
    class Meta:
        model = Cliente
        fields = ('ci',)
        
class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ('ci',)
        
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    first_name = forms.CharField(label="Nombre", max_length=100)
    last_name = forms.CharField(label="Apellido", max_length=100)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'telefono', 'direccion')


    
    

