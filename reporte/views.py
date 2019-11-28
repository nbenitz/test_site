from django.shortcuts import render

import os 
from django.http import HttpResponse
from io import BytesIO
#import xlwt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors, styles
from reserva.models import Reserva
import datetime
from reportlab.platypus.para import Paragraph
from reportlab.lib.units import cm
#from django.http import request

# Create your views here.

def report_reserva(request):
    #Create the HttpResponse headers with PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reporte-reserva.pdf"'
    #Create the pdf object, using the BytesIO object as its "file."
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    # Header
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30,750,'Hotel Amanecer')
    
    c.setFont('Helvetica', 12)
    c.drawString(30,735,'Reporte de Reservas')
    
    c.setFont('Helvetica-Bold', 12)
    c.drawString(480,750, str(datetime.date.today()))
    # start X, height end y, heigth
    c.line(460, 747, 560, 747)
    
    # Tabla Reservas
    reservas = list(Reserva.objects.all())
    
    # Table header
    styles = getSampleStyleSheet()
    styleBH = styles["Normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontSize = 18
    
    cliente = Paragraph('''Cliente''', styleBH)
    habitacion = Paragraph('''Habitacion''', styleBH)
    fecha_entrada = Paragraph('''Entrada''', styleBH)
    fecha_salida = Paragraph('''Salida''', styleBH)
    costo_alojamiento = Paragraph('''Importe''', styleBH)
    
    data = []
    data.append([cliente, habitacion, fecha_entrada, fecha_salida, costo_alojamiento])
    
    # Table body
    styleN = styles["Normal"]
    styleN.alignment = TA_CENTER
    styleN.fontSize = 7
    
    high = 650
    for reserva in reservas:
        this_reserva = [reserva.id_empleado_fk,
                        reserva.id_habitacion_fk,
                        reserva.fecha_entrada,
                        reserva.fecha_salida,
                        reserva.costo_alojamiento,
                        ]
        data.append(this_reserva)
        high = high - 18
        
    # Table size
    width, height = A4
    table = Table(data, colWidths=[4.125 * cm, 2.5 * cm, 4.125 * cm, 4.125 * cm, 4.125 * cm, ])
    table.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]))
    # Pdf size
    table.wrapOn(c, width, height)
    table.drawOn(c, 30, high)    
    
    
    
    # End writing

    c.showPage()
    c.save()
    # get the value of BytesIO buffer and write response
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response