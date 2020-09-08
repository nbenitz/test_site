# from django.shortcuts import render

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Habitacion, CategoriaHab, Proveedor, CategoriaProd, Servicio, Dispositivo
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from estructura.models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from persona.models import Cliente
from reserva.models import Reserva

# Create your views here.

class ObjetoListado(LoginRequiredMixin, ListView): 
    """Lista los objetos model pasado desde urls.py"""
    
class ObjetoDetalle(LoginRequiredMixin, DetailView): 
    """Muestra los detalles del objeto model pasado desde urls.py"""

#=================================== Habitacion ===========================================    
class HabitacionCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = Habitacion  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = Habitacion  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = ['numero', 'precio1', 'id_categoria_fk', 'caracteristicas', 'foto']
    success_message = 'Habitacion Creada Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la pagina principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerHabitacion')  # Redireccionamos a la vista principal 'leer'

 
class HabitacionActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Habitacion  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = Habitacion  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = ['numero', 'precio1', 'id_categoria_fk', 'caracteristicas', 'foto']
    success_message = 'Habitacion Actualizada Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la pagina principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerHabitacion')  # Redireccionamos a la vista principal 'leer'

   
class HabitacionEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = Habitacion 
    form = Habitacion
    fields = "__all__"     
 
    # Redireccionamos a la pagina principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Proveedor Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerProveedor')  # Redireccionamos a la vista principal 'leer'

    
class ProveedorCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = Proveedor  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = Proveedor  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Proveedor Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la pagina principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerProveedor')  # Redireccionamos a la vista principal 'leer'

 
class ProveedorActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Proveedor  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = Proveedor  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Proveedor Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la pagina principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerProveedor')  # Redireccionamos a la vista principal 'leer'

   
class ProveedorEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = Proveedor 
    form = Proveedor
    fields = "__all__"     
 
    # Redireccionamos a la pagina principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Proveedor Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerProveedor')  # Redireccionamos a la vista principal 'leer'

    
class ProductoCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = Producto  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = Producto  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = ['barcode', 'descripcion', 'costo', 'precio1', 'stock', 'presentacion', 'foto', 'iva', 'id_categoria_fk', 'id_proveedor_fk']
    success_message = 'Producto Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la pagina principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerProducto')  # Redireccionamos a la vista principal 'leer'
    
 
class ProductoActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Producto  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = Producto  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = ['barcode', 'descripcion', 'costo', 'precio1', 'stock', 'presentacion', 'foto', 'iva', 'id_categoria_fk', 'id_proveedor_fk']
    success_message = 'Producto Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la pagina principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerProducto')  # Redireccionamos a la vista principal 'leer'

   
class ProductoEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = Producto 
    form = Producto
    fields = "__all__"     
 
    # Redireccionamos a la pagina principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerProducto')  # Redireccionamos a la vista principal 'leer'


class CategoriaHabCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = CategoriaHab  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = CategoriaHab  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Categoria Habitacion Creada Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la pagina principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerCategoriaHab')  # Redireccionamos a la vista principal 'leer'
    
 
class CategoriaHabActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = CategoriaHab  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = CategoriaHab  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Categoria Habitacion Actualizada Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la pagina principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerCategoriaHab')  # Redireccionamos a la vista principal 'leer'

   
class CategoriaHabEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = CategoriaHab 
    form = CategoriaHab
    fields = "__all__"     
 
    # Redireccionamos a la pagina principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Categoria Habitacion Eliminada Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerCategoriaHab')  # Redireccionamos a la vista principal 'leer'

    
class CategoriaProdCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = CategoriaProd  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = CategoriaProd  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Categoria Producto Creada Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la pagina principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerCategoriaProd')  # Redireccionamos a la vista principal 'leer'
    
 
class CategoriaProdActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = CategoriaProd  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = CategoriaProd  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Categoria Producto Actualizada Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la pagina principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerCategoriaProd')  # Redireccionamos a la vista principal 'leer'

   
class CategoriaProdEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = CategoriaProd 
    form = CategoriaProd
    fields = "__all__"     
 
    # Redireccionamos a la pagina principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Categoria Producto Eliminada Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerCategoriaProd')  # Redireccionamos a la vista principal 'leer'


class ServicioCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = Servicio  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = Servicio  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Servicio Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la pagina principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerServicio')  # Redireccionamos a la vista principal 'leer'

 
class ServicioActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Servicio  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = Servicio  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Servicio Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la pagina principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerServicio')  # Redireccionamos a la vista principal 'leer'

   
class ServicioEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = Servicio 
    form = Servicio
    fields = "__all__"     
 
    # Redireccionamos a la pagina principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Servicio Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerServicio')  # Redireccionamos a la vista principal 'leer'


class DispositivoCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = Dispositivo 
    form = Dispositivo
    fields = ['id_habitacion_fk', 'tipo', 'descripcion']
    success_message = 'Dispositivo Creado Correctamente !'
 
    def get_success_url(self):        
        return reverse('leerDispositivo')

 
class DispositivoActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Dispositivo
    form = Dispositivo
    fields = ['id_habitacion_fk', 'tipo', 'descripcion']
    success_message = 'Dispositivo Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('leerDispositivo')


class DispositivoEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = Dispositivo 
    form = Dispositivo
    fields = "__all__"

    def get_success_url(self): 
        success_message = 'Dispositivo Eliminado Correctamente !'
        messages.success (self.request, (success_message))       
        return reverse('leerDispositivo')


class Tablero(LoginRequiredMixin, ListView): 
    model = Dispositivo

    def get_queryset(self, **kwargs):
        qs = self.model.objects.none()
        if self.request.user.is_client:
            cliente = Cliente.objects.get(user_id=self.request.user.id)
            reserva_cliente_ocupado = Reserva.objects.filter(
                    id_cliente_fk=cliente.id,
                    estado="Ocupado"
                    )
            print(reserva_cliente_ocupado)
            if reserva_cliente_ocupado.exists():
                id_hab = reserva_cliente_ocupado.values_list('id_habitacion_fk', flat=True)[0]
                qs = self.model.objects.filter(id_habitacion_fk=id_hab)
                print(qs)
        return qs

