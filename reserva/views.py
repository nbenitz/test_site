from io import BytesIO
#import xlwt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors, styles
from reportlab.platypus.para import Paragraph
from reportlab.lib.units import cm

from django.shortcuts import render, get_object_or_404, redirect, reverse
from reserva.models import Reserva, DetalleVentaProd, Pago
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse
from persona.models import Empleado, Cliente
import json
import datetime
from django.db.models import Max

from reserva.forms import ReservaForm, PagoForm
from django.http import HttpResponse, JsonResponse
from estructura.models import Habitacion, CategoriaHab, Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from reserva.tables import ProductTable, DetVentaProdTable
from django_tables2.config import RequestConfig
from django.template.loader import render_to_string


# Create your views here.
#=================================== Reserva ===========================================
class ReservaCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    form_class = ReservaForm 
    success_message = 'Reserva Creada Correctamente !' 
    
    # Sending user object to the form, to verify which fields to display/remove
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
        return reverse('leerReserva', args=['crear',])

    
def load_precio(request):
    id_habitacion = request.GET.get('habitacion')
    precio = Habitacion.objects.filter(id_habitacion=id_habitacion).values_list('precio1', flat=True)[0]
    return HttpResponse(precio)

def load_habitacion_disponible(request):
    entrada = request.GET.get('entrada')
    salida = request.GET.get('salida')
    
    habitaciones = Habitacion.objects.all()
    
    hab_reservada = Reserva.objects.exclude(
        estado="Anulado"
        ).filter(
            fecha_entrada__gte=entrada, 
            fecha_entrada__lt=salida
            )|Reserva.objects.exclude(
                estado="Anulado"
                ).filter(
                    fecha_salida__gt=entrada, 
                    fecha_salida__lte=salida
                    )|Reserva.objects.exclude(
                        estado="Anulado"
                        ).filter(
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
    
    def get_queryset(self, **kwargs):
        operacion = self.kwargs['operacion']
        qs = self.model.objects.exclude(estado="Anulado")
        #qs = Reserva.no_anuladas(Reserva.objects.all())
        if self.request.user.is_client:
            cliente = Cliente.objects.get(user_id=self.request.user.id)
            qs = qs.filter(id_cliente_fk=cliente)
        if operacion == "anular":
            qs = qs.filter(fecha_entrada__gte=datetime.date.today())
        if operacion == "confirmar":
            qs = qs.filter(fecha_entrada=datetime.date.today())
        if operacion == "finalizar":
            qs = qs.filter(fecha_salida__lte=datetime.date.today(), estado="Confirmado")
        elif operacion == "pago" or operacion == "consumo" or operacion == "ampliar" or operacion == "crear":
            qs = qs.filter(fecha_salida__gte=datetime.date.today())    
        
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operacion"] = self.kwargs['operacion']
        return context
    
class ReservaDetalle(LoginRequiredMixin, DetailView):
    model = Reserva
    extra_context = {'titulo':'Detalles de la Reserva'}
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operacion"] = self.kwargs['operacion']
        return context

class ReservaConfirmar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Reserva 
    form = Reserva 
    fields = []
    success_message = 'Reserva Confirmada Correctamente !'
    
    def form_valid(self, form):
        form.instance.estado = "Confirmado"
        return super().form_valid(form)
 
    def get_success_url(self):
        return reverse('leerReserva', args=['confirmar',])


class ReservaFinalizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Reserva 
    form = Reserva 
    fields = []
    success_message = 'Reserva Finalizada Correctamente !'
    
    def form_valid(self, form):
        form.instance.estado = "Finalizado"
        return super().form_valid(form)
 
    def get_success_url(self):
        return reverse('leerReserva', args=['finalizar',])
       
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
    fields = ['fecha_entrada', 'fecha_salida', 'costo_alojamiento',]
    success_message = 'Reserva Ampliada Correctamente !'
    #extra_context={'fecha_salida_max': 'Fecha_salida_max'}
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
               
        id_habitacion = Reserva.objects.filter(id_reserva=self.kwargs['pk']).values_list('id_habitacion_fk', flat=True)[0]
        fecha_salida = Reserva.objects.filter(id_reserva=self.kwargs['pk']).values_list('fecha_salida', flat=True)[0]
        
        fecha_salida_max = ""
        qs = Reserva.objects.exclude(
            id_reserva=self.kwargs['pk']
            ).filter(
                id_habitacion_fk=id_habitacion,
                fecha_entrada__gte=fecha_salida
                ).order_by('fecha_entrada'
                           ).values_list('fecha_entrada', flat=True)
        if qs.exists():
            fecha_salida_max = qs[0]
            print(fecha_salida_max)
        else:
            print("No hay resultados")
        
        print(qs)
        context["fecha_salida_max"] = str(fecha_salida_max)
        return context

    def get_success_url(self):
        return reverse('leerReserva', args=['ampliar',])
    
class DetalleVenta(ListView):
    model = DetalleVentaProd

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = Reserva.objects.get(id_reserva=self.kwargs['pk'])
        qs_p = Producto.objects.filter(is_active=True)[:6]
        products = ProductTable(qs_p)
        detalle_venta_prod = DetVentaProdTable(instance.detalle_venta_prod.all())
        RequestConfig(self.request).configure(products)
        RequestConfig(self.request).configure(detalle_venta_prod)
        context.update(locals())
        return context
    
    

def ajax_add_product(request, pk, dk):
    instance = get_object_or_404(Reserva, id_reserva=pk)
    product = get_object_or_404(Producto, id_producto=dk)
    detalle_venta_prod, created = DetalleVentaProd.objects.get_or_create(id_reserva_fk=instance, id_producto_fk=product)
    if created:
        detalle_venta_prod.cantidad = 1
        detalle_venta_prod.precio = product.precio1
    else:
        detalle_venta_prod.cantidad += 1
    detalle_venta_prod.save()
    product.stock -= 1
    product.save()
    instance.refresh_from_db()
    detalle_venta_prod = DetVentaProdTable(instance.detalle_venta_prod.all())
    RequestConfig(request).configure(detalle_venta_prod)
    data = dict()
    data['result'] = render_to_string(template_name='include/order_container.html',
                                      request=request,
                                      context={'instance': instance,
                                               'detalle_venta_prod': detalle_venta_prod
                                               }
                                    )
    return JsonResponse(data)



def ajax_modify_detalle_venta_prod(request, pk, action):
    detalle_venta_prod = get_object_or_404(DetalleVentaProd, id_detalle_venta=pk)
    product = detalle_venta_prod.id_producto_fk
    instance = detalle_venta_prod.id_reserva_fk
    if action == 'remove':
        detalle_venta_prod.cantidad -= 1
        product.stock += 1
        if detalle_venta_prod.cantidad < 1: detalle_venta_prod.cantidad = 1
    if action == 'add':
        detalle_venta_prod.cantidad += 1
        product.stock -= 1
    product.save()
    detalle_venta_prod.save()
    if action == 'delete':
        detalle_venta_prod.delete()
    data = dict()
    instance.refresh_from_db()
    detalle_venta_prod = DetVentaProdTable(instance.detalle_venta_prod.all())
    RequestConfig(request).configure(detalle_venta_prod)
    data['result'] = render_to_string(template_name='include/order_container.html',
                                      request=request,
                                      context={
                                          'instance': instance,
                                          'detalle_venta_prod': detalle_venta_prod
                                      }
                                      )
    return JsonResponse(data)



def ajax_search_products(request, pk):
    instance = get_object_or_404(Reserva, id_reserva=pk)
    q = request.GET.get('q', None)
    products = Producto.broswer.is_active().filter(
        barcode__icontains=q
        )|Producto.broswer.is_active().filter(
            descripcion__icontains=q
            ) if q else Producto.broswer.is_active()
    products = products[6]
    products = ProductTable(products)
    RequestConfig(request).configure(products)
    data = dict()
    data['products'] = render_to_string(template_name='include/product_container.html',
                                        request=request,
                                        context={
                                            'products': products,
                                            'instance': instance
                                        })
    return JsonResponse(data)

"""
class DetallePago(LoginRequiredMixin, DetailView):
    model = Reserva
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reserva = self.model.objects.get(id_reserva=self.kwargs['pk'])
        detalle_venta_prod = reserva.detalle_venta_prod.all()
        context.update(locals())
        return context
"""

class DetallePago(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = PagoForm
    success_message = 'Pago Registrado Correctamente !'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reserva = Reserva.objects.get(id_reserva=self.kwargs['pk'])
        detalle_venta_prod = reserva.detalle_venta_prod.all()
        context.update(locals())
        return context
    
    # Sending reserva object to the form
    def get_form_kwargs(self):
        kwargs = super(DetallePago, self).get_form_kwargs()
        reserva = Reserva.objects.get(id_reserva=self.kwargs['pk'])
        kwargs.update({'reserva': reserva})
        return kwargs
    
    def form_valid(self, form):
        reserva = Reserva.objects.get(id_reserva=self.kwargs['pk'])
        form.instance.id_reserva = reserva
        return super().form_valid(form)
    
    def get_success_url(self):
        reserva = Reserva.objects.get(id_reserva=self.kwargs['pk'])
        saldo_pendiente = Reserva.saldo_pendiente(reserva)
        #total = Reserva.total(reserva)
        id_pago = reserva.pagos.aggregate(Max('id_pago'))['id_pago__max']
        pago = Pago.objects.filter(id_pago=id_pago).values_list('total_pago', flat=True)[0]
        #saldo_anterior = saldo_actual - pago
        #total_pagado = saldo_anterior + pago
        
        vuelto = 0
        if saldo_pendiente < 0:
            vuelto = saldo_pendiente * -1
            debito = pago - vuelto
            Pago.objects.filter(id_pago=id_pago).update(total_pago=debito)
        
        print(vuelto)
        return reverse('factura', args=[self.kwargs['pk'], pago, vuelto, ])
    

def factura(request, pk, pago, vuelto):
    #Create the HttpResponse headers with PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reporte-reserva.pdf"'
    #Create the pdf object, using the BytesIO object as its "file."
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    
    # Tabla Reservas
    reserva = Reserva.objects.get(id_reserva=pk)
    detalle_venta_prod = reserva.detalle_venta_prod.all()

    # Header
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30,750,'Hotel Amanecer')
    
    c.setFont('Helvetica', 12)
    c.drawString(30,730, f'{"Factura - "} {reserva.id_reserva}')
    c.drawString(30,710, f'{"Costo de Alojamiento: "} {reserva.tag_costo_alojamiento()}')
    c.drawString(300,710, f'{"Consumo: "} {reserva.tag_total_consumo()}')
    c.drawString(30,690, f'{"Total: "} {reserva.tag_total()}')
    c.drawString(30,670, f'{"Total Abonado: "} {reserva.tag_total_pagos()}')
    c.drawString(300,670, f'{"Saldo Pendiente: "} {reserva.tag_saldo_pendiente()}')
    #c.drawString(30,675, f'{"Monto Pagado: "} {"..."}')
    #c.drawString(300,675, f'{"Vuelto: "} {"..."}')
    
    
    c.setFont('Helvetica-Bold', 12)
    c.drawString(480,750, str(datetime.date.today()))
    # start X, height end y, heigth
    c.line(460, 747, 560, 747)
    
    # Table header
    styles = getSampleStyleSheet()
    styleBH = styles["Normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontSize = 18
    
    producto = Paragraph('''Producto''', styleBH)
    cantidad = Paragraph('''Cantidad''', styleBH)
    precio = Paragraph('''Precio''', styleBH)
    subtotal = Paragraph('''Subtotal''', styleBH)
    
    data = []
    data.append([producto, cantidad, precio, subtotal])
    
    # Table body
    styleN = styles["Normal"]
    styleN.alignment = TA_CENTER
    styleN.fontSize = 7
    
    high = 630
    for consumo in detalle_venta_prod:
        this_consumo = [consumo.id_producto_fk,
                        consumo.tag_cantidad(),
                        consumo.tag_precio(),
                        consumo.tag_sub_total()
                        ]
        data.append(this_consumo)
        high = high - 18
        
    # Table size
    width, height = A4
    table = Table(data, colWidths=[4.75 * cm, 4.75 * cm, 4.75 * cm, 4.75 * cm, 4.75 * cm])
    table.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]))
    # Pdf size
    table.wrapOn(c, width, height)
    table.drawOn(c, 30, high)
    
    high = high - 35
    
    c.drawString(30,high, f'{"Monto Pagado: "} {pago}')
    if int(vuelto) > 0:
        c.drawString(300,high, f'{"Vuelto: "} {vuelto}')  
    
    
    
    # End writing

    c.showPage()
    c.save()
    # get the value of BytesIO buffer and write response
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

class HabDispListado(LoginRequiredMixin, ListView):
    model = Reserva
    #extra_context={'titulo': 'Anular Reserva'}
    
    def get_queryset(self, **kwargs):
        qs = self.model.objects.exclude(estado="Anulado")
        
        if self.request.user.is_client:
            cliente = Cliente.objects.get(user_id=self.request.user.id)
            qs = qs.filter(id_cliente_fk=cliente)
        if operacion == "anular":
            qs = qs.filter(fecha_entrada__gte=datetime.date.today())
        elif operacion == "pago" or operacion == "consumo" or operacion == "ampliar" or operacion == "crear":
            qs = qs.filter(fecha_salida__gte=datetime.date.today())    
        
        return qs