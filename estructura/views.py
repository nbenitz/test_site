# from django.shortcuts import render

# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
# Instanciamos los modelos para poder usarlo en nuestras Vistas CRUD
from .models import Habitacion, CategoriaHab, Proveedor, CategoriaProd, Servicio

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
from estructura.models import Producto
 
# Habilitamos los formularios en Django
# from django import forms


# Create your views here.
#=================================== Habitacion ===========================================
class HabitacionListado(ListView): 
    model = Habitacion  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    # paginate_by = 10

    
class HabitacionCrear(SuccessMessageMixin, CreateView): 
    model = Habitacion  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = Habitacion  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Habitacion Creada Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerHabitacion')  # Redireccionamos a la vista principal 'leer'

    
class HabitacionDetalle(DetailView): 
    model = Habitacion  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'

 
class HabitacionActualizar(SuccessMessageMixin, UpdateView): 
    model = Habitacion  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = Habitacion  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Habitacion Actualizada Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerHabitacion')  # Redireccionamos a la vista principal 'leer'

   
class HabitacionEliminar(SuccessMessageMixin, DeleteView): 
    model = Habitacion 
    form = Habitacion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Proveedor Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerProveedor')  # Redireccionamos a la vista principal 'leer'
    
class ProveedorListado(ListView): 
    model = Proveedor  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    # paginate_by = 10

    
class ProveedorCrear(SuccessMessageMixin, CreateView): 
    model = Proveedor  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = Proveedor  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Proveedor Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerProveedor')  # Redireccionamos a la vista principal 'leer'

    
class ProveedorDetalle(DetailView): 
    model = Proveedor  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'

 
class ProveedorActualizar(SuccessMessageMixin, UpdateView): 
    model = Proveedor  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = Proveedor  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Proveedor Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerProveedor')  # Redireccionamos a la vista principal 'leer'

   
class ProveedorEliminar(SuccessMessageMixin, DeleteView): 
    model = Proveedor 
    form = Proveedor
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Proveedor Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerProveedor')  # Redireccionamos a la vista principal 'leer'


class ProductoListado(ListView): 
    model = Producto  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    # paginate_by = 10

    
class ProductoCrear(SuccessMessageMixin, CreateView): 
    model = Producto  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = Producto  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Producto Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerProducto')  # Redireccionamos a la vista principal 'leer'

    
class ProductoDetalle(DetailView): 
    model = Producto  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'

 
class ProductoActualizar(SuccessMessageMixin, UpdateView): 
    model = Producto  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = Producto  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Producto Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerProducto')  # Redireccionamos a la vista principal 'leer'

   
class ProductoEliminar(SuccessMessageMixin, DeleteView): 
    model = Producto 
    form = Producto
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerProducto')  # Redireccionamos a la vista principal 'leer'


class CategoriaHabListado(ListView): 
    model = CategoriaHab  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    # paginate_by = 10

    
class CategoriaHabCrear(SuccessMessageMixin, CreateView): 
    model = CategoriaHab  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = CategoriaHab  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Categoria Habitacion Creada Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerCategoriaHab')  # Redireccionamos a la vista principal 'leer'

    
class CategoriaHabDetalle(DetailView): 
    model = CategoriaHab  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'

 
class CategoriaHabActualizar(SuccessMessageMixin, UpdateView): 
    model = CategoriaHab  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = CategoriaHab  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Categoria Habitacion Actualizada Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerCategoriaHab')  # Redireccionamos a la vista principal 'leer'

   
class CategoriaHabEliminar(SuccessMessageMixin, DeleteView): 
    model = CategoriaHab 
    form = CategoriaHab
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Categoria Habitacion Eliminada Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerCategoriaHab')  # Redireccionamos a la vista principal 'leer'

class CategoriaProdListado(ListView): 
    model = CategoriaProd  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    # paginate_by = 10

    
class CategoriaProdCrear(SuccessMessageMixin, CreateView): 
    model = CategoriaProd  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = CategoriaProd  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Categoria Producto Creada Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerCategoriaProd')  # Redireccionamos a la vista principal 'leer'

    
class CategoriaProdDetalle(DetailView): 
    model = CategoriaProd  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'

 
class CategoriaProdActualizar(SuccessMessageMixin, UpdateView): 
    model = CategoriaProd  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = CategoriaProd  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Categoria Producto Actualizada Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerCategoriaProd')  # Redireccionamos a la vista principal 'leer'

   
class CategoriaProdEliminar(SuccessMessageMixin, DeleteView): 
    model = CategoriaProd 
    form = CategoriaProd
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Categoria Producto Eliminada Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerCategoriaProd')  # Redireccionamos a la vista principal 'leer'


class ServicioListado(ListView): 
    model = Servicio  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    # paginate_by = 10

    
class ServicioCrear(SuccessMessageMixin, CreateView): 
    model = Servicio  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'
    form = Servicio  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Servicio Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leerServicio')  # Redireccionamos a la vista principal 'leer'

    
class ServicioDetalle(DetailView): 
    model = Servicio  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py'

 
class ServicioActualizar(SuccessMessageMixin, UpdateView): 
    model = Servicio  # Llamamos a la clase 'Habitacion' que se encuentra en nuestro archivo 'models.py' 
    form = Servicio  # Definimos nuestro formulario con el nombre de la clase o modelo 'Habitacion' 
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Habitacion' de nuestra Base de Datos 
    success_message = 'Servicio Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leerServicio')  # Redireccionamos a la vista principal 'leer'

   
class ServicioEliminar(SuccessMessageMixin, DeleteView): 
    model = Servicio 
    form = Servicio
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Habitacion
    def get_success_url(self): 
        success_message = 'Servicio Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Habitacion 
        messages.success (self.request, (success_message))       
        return reverse('leerServicio')  # Redireccionamos a la vista principal 'leer'
