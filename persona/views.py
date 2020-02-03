
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib import messages 
from django.contrib.auth import get_user_model, authenticate, login
from persona.forms import UserForm, ClienteForm, EmpleadoForm, SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from persona.tokens import account_activation_token
from django.conf import settings




# Create your views here.


#=================================== CLIENTE ===========================================
class ClienteListado(LoginRequiredMixin, ListView): 
    model = get_user_model()  # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py'
    
    def get_queryset(self):
        qs = self.model.objects.filter(is_client=1)
        return qs
    
    
class ClienteDetalle(DetailView): 
    model = get_user_model()
    
    
def create_client(request):
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='UF')
        cliente_form = ClienteForm(request.POST, prefix='PF')
            
        if user_form.is_valid() and cliente_form.is_valid():         
            user = user_form.save(commit=False)
            user_form.instance.is_client = True
            user.save()
    
            user.cliente.ci = cliente_form.cleaned_data.get('ci')
            user.cliente.save()
            messages.success(request, ('Cliente creado correctmente'))
            return redirect('leerCliente')
            
    else:
        user_form = UserForm(prefix='UF')
        cliente_form = ClienteForm(prefix='PF')
        
    return render(request, 'cliente/crear.html',{
        'user_form': user_form,
        'cliente_form': cliente_form,
        })
    
def edit_client(request, pk):
    
    user = get_user_model().objects.get(id=pk)
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='UF', instance=user)
        cliente_form = ClienteForm(request.POST, prefix='PF', instance=user.cliente)
            
        if user_form.is_valid() and cliente_form.is_valid():
            user = user_form.save(commit=False)
            user_form.instance.is_client = True
            user.save()
    
            user.cliente.ci = cliente_form.cleaned_data.get('ci')
            user.cliente.save()
            messages.success(request, ('Cliente actualizado correctmente'))
            return redirect('leerCliente')
            
    else:
        user_form = UserForm(prefix='UF', instance=user)
        cliente_form = ClienteForm(prefix='PF', instance=user.cliente)
        
    return render(request, 'cliente/crear.html',{
        'user_form': user_form,
        'cliente_form': cliente_form,
        })
    
    
    
#=================================== EMPLEADO ===========================================

class EmpleadoListado(ListView): 
    model = get_user_model() 
    
    def get_queryset(self):
        qs = self.model.objects.filter(is_client=0)
        return qs
    
    
class EmpleadoDetalle(DetailView): 
    model = get_user_model()
    
    
def create_empleado(request):
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='UF')
        empleado_form = EmpleadoForm(request.POST, prefix='PF')
            
        if user_form.is_valid() and empleado_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
    
            user.empleado.ci = empleado_form.cleaned_data.get('ci')
            user.empleado.save()
            messages.success(request, ('Empleado creado correctmente'))
            return redirect('leerEmpleado')
            
    else:
        user_form = UserForm(prefix='UF')
        empleado_form = ClienteForm(prefix='PF')
        
    return render(request, 'empleado/crear.html',{
        'user_form': user_form,
        'empleado_form': empleado_form,
        })


def edit_empleado(request, pk):
    
    user = get_user_model().objects.get(id=pk)
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='UF', instance=user)
        empleado_form = EmpleadoForm(request.POST, prefix='PF', instance=user.empleado)
            
        if user_form.is_valid() and empleado_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
    
            user.empleado.ci = empleado_form.cleaned_data.get('ci')
            user.empleado.save()
            messages.success(request, ('Cliente actualizado correctmente'))
            return redirect('leerEmpleado')
            
    else:
        user_form = UserForm(prefix='UF', instance=user)
        empleado_form = EmpleadoForm(prefix='PF', instance=user.empleado)
        
    return render(request, 'empleado/crear.html',{
        'user_form': user_form,
        'empleado_form': empleado_form,
        })
#=================================== USUARIO ===========================================
class UsuarioListado(ListView): 
    model = get_user_model() 
    
class UsuarioDetalle(DetailView): 
    model = get_user_model()
    
    
def create_client2(request):
    
    if request.method == 'POST':
        user_form = SignUpForm(request.POST, prefix='UF')
        cliente_form = ClienteForm(request.POST, prefix='PF')
            
        if user_form.is_valid() and cliente_form.is_valid():         
            user = user_form.save(commit=False)
            user_form.instance.is_client = True
            user_form.instance.is_active = False
            user.save()
    
            user.cliente.ci = cliente_form.cleaned_data.get('ci')
            user.cliente.save()
            #messages.success(request, ('Cliente creado correctmente'))
            #return redirect('leerCliente')
            
            
            current_site = get_current_site(request)
            subject = 'Por favor activa tu cuenta'
            email_from = settings.EMAIL_HOST_USER
            message = render_to_string('registration/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message, email_from)
        
            return redirect('activation_send')
            
            
    else:
        user_form = SignUpForm(prefix='UF')
        cliente_form = ClienteForm(prefix='PF')
        
    return render(request, 'cliente/crear.html',{
        'user_form': user_form,
        'cliente_form': cliente_form,
        })


def signup_view(request):
    user_form = SignUpForm(request.POST, prefix='UF')
    cliente_form = ClienteForm(request.POST, prefix='PF')
    
    if user_form.is_valid() and cliente_form.is_valid():
        user = user_form.save(commit=False)
        user_form.instance.is_client = True
        user_form.instance.is_active = False
        user.save()
    
        user.cliente.ci = cliente_form.cleaned_data.get('ci')
        user.cliente.save()
        
        
        current_site = get_current_site(request)
        subject = 'Por favor activa tu cuenta'
        email_from = settings.EMAIL_HOST_USER
        # load a template like get_template() 
        # and calls its render() method immediately.
        message = render_to_string('registration/activation_request.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            # method will generate a hash value with user related data
            'token': account_activation_token.make_token(user),
        })
        user.email_user(subject, message, email_from)
        
        
        
        return redirect('activation_send')
    
    
    else:
        user_form = SignUpForm(prefix='UF')
        cliente_form = ClienteForm(prefix='PF')
    return render(request,
                  'registration/registration_form.html',
                  {'user_form': user_form,
                   'cliente_form': cliente_form,})
    
    
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true 
        user.is_active = True
        # set signup_confirmation true
        user.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('activation_complete')
    else:
        return render(request, 'activation_invalid.html')
    
def activation_sent_view(request):
    return render(request, 'registration/registration_complete.html')

def activation_complete_view(request):
    return render(request, 'registration/activation_complete.html')
