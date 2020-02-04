# from django.shortcuts import render

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Habitacion, CategoriaHab, Proveedor, CategoriaProd, Servicio
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from estructura.models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
#=================================== Habitacion ===========================================
class HabitacionListado(LoginRequiredMixin, ListView): 
    model = Habitacion  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    # paginate_by = 10

    
class HabitacionCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = Habitacion  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = Habitacion  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Habitacion Creada Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerHabitacion')  # Redireccionamos a la vista principal 'leer'


class HabitacionDetalle(LoginRequiredMixin, DetailView): 
    model = Habitacion  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'

 
class HabitacionActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Habitacion  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = Habitacion  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Habitacion Actualizada Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerHabitacion')  # Redireccionamos a la vista principal 'leer'

   
class HabitacionEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = Habitacion 
    form = Habitacion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Proveedor Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerProveedor')  # Redireccionamos a la vista principal 'leer'
    
class ProveedorListado(LoginRequiredMixin, ListView): 
    model = Proveedor  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    # paginate_by = 10

    
class ProveedorCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = Proveedor  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = Proveedor  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Proveedor Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerProveedor')  # Redireccionamos a la vista principal 'leer'

    
class ProveedorDetalle(LoginRequiredMixin, DetailView): 
    model = Proveedor  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'

 
class ProveedorActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Proveedor  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = Proveedor  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Proveedor Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerProveedor')  # Redireccionamos a la vista principal 'leer'

   
class ProveedorEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = Proveedor 
    form = Proveedor
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Proveedor Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerProveedor')  # Redireccionamos a la vista principal 'leer'


class ProductoListado(LoginRequiredMixin, ListView): 
    model = Producto  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    # paginate_by = 10

    
class ProductoCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = Producto  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = Producto  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = ['barcode', 'descripcion', 'costo', 'precio1', 'stock', 'presentacion', 'foto', 'iva', 'id_categoria_fk', 'id_proveedor_fk']
    success_message = 'Producto Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerProducto')  # Redireccionamos a la vista principal 'leer'

    
class ProductoDetalle(LoginRequiredMixin, DetailView): 
    model = Producto  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'

 
class ProductoActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Producto  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = Producto  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = ['barcode', 'descripcion', 'costo', 'precio1', 'stock', 'presentacion', 'foto', 'iva', 'id_categoria_fk', 'id_proveedor_fk']
    success_message = 'Producto Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerProducto')  # Redireccionamos a la vista principal 'leer'

   
class ProductoEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = Producto 
    form = Producto
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerProducto')  # Redireccionamos a la vista principal 'leer'


class CategoriaHabListado(LoginRequiredMixin, ListView): 
    model = CategoriaHab  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    # paginate_by = 10

    
class CategoriaHabCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = CategoriaHab  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = CategoriaHab  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Categoria Habitacion Creada Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerCategoriaHab')  # Redireccionamos a la vista principal 'leer'

    
class CategoriaHabDetalle(LoginRequiredMixin, DetailView): 
    model = CategoriaHab  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'

 
class CategoriaHabActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = CategoriaHab  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = CategoriaHab  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Categoria Habitacion Actualizada Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerCategoriaHab')  # Redireccionamos a la vista principal 'leer'

   
class CategoriaHabEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = CategoriaHab 
    form = CategoriaHab
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Categoria Habitacion Eliminada Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerCategoriaHab')  # Redireccionamos a la vista principal 'leer'

class CategoriaProdListado(LoginRequiredMixin, ListView): 
    model = CategoriaProd  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    # paginate_by = 10

    
class CategoriaProdCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = CategoriaProd  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = CategoriaProd  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Categoria Producto Creada Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerCategoriaProd')  # Redireccionamos a la vista principal 'leer'

    
class CategoriaProdDetalle(LoginRequiredMixin, DetailView): 
    model = CategoriaProd  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'

 
class CategoriaProdActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = CategoriaProd  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = CategoriaProd  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Categoria Producto Actualizada Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerCategoriaProd')  # Redireccionamos a la vista principal 'leer'

   
class CategoriaProdEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = CategoriaProd 
    form = CategoriaProd
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Categoria Producto Eliminada Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerCategoriaProd')  # Redireccionamos a la vista principal 'leer'


class ServicioListado(LoginRequiredMixin, ListView): 
    model = Servicio  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    # paginate_by = 10

    
class ServicioCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = Servicio  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = Servicio  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Servicio Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerServicio')  # Redireccionamos a la vista principal 'leer'

    
class ServicioDetalle(LoginRequiredMixin, DetailView): 
    model = Servicio  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'

 
class ServicioActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Servicio  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = Servicio  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Servicio Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerServicio')  # Redireccionamos a la vista principal 'leer'

   
class ServicioEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = Servicio 
    form = Servicio
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Servicio Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerServicio')  # Redireccionamos a la vista principal 'leer'
