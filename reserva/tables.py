import django_tables2 as tables

from estructura.models import Producto
from .models import DetalleVentaProd, Reserva


class OrderTable(tables.Table):
    tag_costo_alojamiento = tables.Column(orderable=False, verbose_name='Costo Alojamiento')
    action = tables.TemplateColumn(
        '<a href="{{ record.get_edit_url }}" class="btn btn-info"><i class="fa fa-edit"></i></a>', orderable=False)

    class Meta:
        model = Reserva
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['fecha_entrada', 'descripcion', 'tag_costo_alojamiento']


class ProductTable(tables.Table):
    tag_precio = tables.Column(orderable=False, verbose_name='Precio')
    action = tables.TemplateColumn(
        '<button class="btn btn-info add_button" data-href="{% url "ajax_add" instance.id_reserva record.id_producto %}">Agregar</a>',
        orderable=False,
        verbose_name='Acción'
    )

    class Meta:
        model = Producto
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['descripcion', 'tag_precio']


class DetVentaProdTable(tables.Table):
    tag_cantidad = tables.Column(orderable=False, verbose_name='Cantidad')
    tag_precio = tables.Column(orderable=False, verbose_name='Precio')
    tag_sub_total = tables.Column(orderable=False, verbose_name='Subtotal')
    action = tables.TemplateColumn('''
            <button data-href="{% url "ajax_modify" record.id_detalle_venta "add" %}" class="btn btn-success edit_button"><i class="fa fa-arrow-up"></i></button>
            <button data-href="{% url "ajax_modify" record.id_detalle_venta "remove" %}" class="btn btn-warning edit_button"><i class="fa fa-arrow-down"></i></button>
            <button data-href="{% url "ajax_modify" record.id_detalle_venta "delete" %}" class="btn btn-danger edit_button"><i class="fa fa-trash"></i></button>
    ''', orderable=False,
        verbose_name='Acción')

    class Meta:
        model = DetalleVentaProd
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['id_producto_fk', 'tag_cantidad', 'tag_precio', 'tag_sub_total']
        
        
        