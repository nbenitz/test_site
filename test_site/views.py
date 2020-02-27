from django.conf import settings
from django.core.mail import send_mail 

from .forms import ContactForm
from django.shortcuts import render
from django.core import management
from django.core.management.commands import loaddata


# Create your views here.


def inicio(request):
    return render(request, "inicio.html", {})


def about(request):
    #management.call_command('dumpdata', 'estructura', output='estructura/fixtures/db.json', format='json')
    management.call_command('loaddata', 'db.json', format='json', app_label='estructura')
    return render(request, "about.html")
    loaddata

def contact(request):
    titulo = "Contacto"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.items():
        #    print(key, value)
        # for key in form.cleaned_data:
        #    print(key)
        #    print(form.cleaned_data.get(key))
        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = 'Form de Contacto'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "n.benitez.a@hotmail.com"]
        email_mensaje = "%s: %s enviado por %s" % (form_nombre, form_mensaje, form_email)
        send_mail(
            asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=False
            )
        print(form_email, email_mensaje, form_nombre)
        
    context = {
        "titulo": titulo,
        "form": form,
    }
    return render(request, "contact.html", context)
    
    

