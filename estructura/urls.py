# estructura/urls.py
from django.urls import path

from .views import HabitacionListado, HabitacionDetalle, HabitacionCrear, HabitacionActualizar, HabitacionEliminar
from estructura.views import ProveedorDetalle, ProveedorListado, ProveedorCrear, ProveedorActualizar, ProveedorEliminar
from estructura.views import ProductoDetalle, ProductoListado, ProductoCrear, ProductoActualizar, ProductoEliminar
from estructura.views import CategoriaHabListado, CategoriaHabDetalle, CategoriaHabCrear, CategoriaHabActualizar, CategoriaHabEliminar 
from estructura.views import CategoriaProdListado, CategoriaProdDetalle, CategoriaProdCrear, CategoriaProdActualizar, CategoriaProdEliminar
from estructura.views import ServicioListado, ServicioDetalle, ServicioCrear, ServicioActualizar, ServicioEliminar

urlpatterns = [
    path('habitacion/', HabitacionListado.as_view(template_name="habitacion/index.html"), name='leerHabitacion'),
    path('habitacion/detalle/<str:pk>', HabitacionDetalle.as_view(template_name="habitacion/detalles.html"), name='detallesHabitacion'),
    path('habitacion/crear', HabitacionCrear.as_view(template_name="habitacion/crear.html"), name='crearHabitacion'),
    path('habitacion/editar/<str:pk>', HabitacionActualizar.as_view(template_name="habitacion/actualizar.html"), name='actualizarHabitacion'),
    path('habitacion/eliminar/<str:pk>', HabitacionEliminar.as_view(), name='eliminarHabitacion'),
    #url de Proveedor
    path('proveedor/', ProveedorListado.as_view(template_name="proveedor/index.html"), name='leerProveedor'),
    path('proveedor/detalle/<str:pk>', ProveedorDetalle.as_view(template_name="proveedor/detalles.html"), name='detallesProveedor'),
    path('proveedor/crear', ProveedorCrear.as_view(template_name="proveedor/crear.html"), name='crearProveedor'),
    path('proveedor/editar/<str:pk>', ProveedorActualizar.as_view(template_name="proveedor/actualizar.html"), name='actualizarProveedor'),
    path('proveedor/eliminar/<str:pk>', ProveedorEliminar.as_view(), name='eliminarProveedor'),
    #url de Producto
    path('producto/', ProductoListado.as_view(template_name="producto/index.html"), name='leerProducto'),
    path('producto/detalle/<str:pk>', ProductoDetalle.as_view(template_name="producto/detalles.html"), name='detallesProducto'),
    path('producto/crear', ProductoCrear.as_view(template_name="producto/crear.html"), name='CrearProducto'),
    path('producto/editar/<str:pk>', ProductoActualizar.as_view(template_name="producto/actualizar.html"), name='actualizarProducto'),
    path('producto/eliminar/<str:pk>', ProductoEliminar.as_view(), name='eliminarProducto'),
    #url de categoria habitacion
    path('categoriahab/', CategoriaHabListado.as_view(template_name="categoriahab/index.html"), name='leerCategoriaHab'),
    path('categoriahab/detalle/<str:pk>', CategoriaHabDetalle.as_view(template_name="categoriahab/detalles.html"), name='detallesCategoriaHab'),
    path('categoriahab/crear', CategoriaHabCrear.as_view(template_name="categoriahab/crear.html"), name='CrearCategoriaHab'),
    path('categoriahab/editar/<str:pk>', CategoriaHabActualizar.as_view(template_name="categoriahab/actualizar.html"), name='actualizarCategoriaHab'),
    path('categoriahab/eliminar/<str:pk>', CategoriaHabEliminar.as_view(), name='eliminarCategoriaHab'),
    #url de categoria producto
    path('categoriaprod/', CategoriaProdListado.as_view(template_name="categoriaprod/index.html"), name='leerCategoriaProd'),
    path('categoriaprod/detalle/<str:pk>', CategoriaProdDetalle.as_view(template_name="categoriaprod/detalles.html"), name='detallesCategoriaProd'),
    path('categoriaprod/crear', CategoriaProdCrear.as_view(template_name="categoriaprod/crear.html"), name='CrearCategoriaProd'),
    path('categoriaprod/editar/<str:pk>', CategoriaProdActualizar.as_view(template_name="categoriaprod/actualizar.html"), name='actualizarCategoriaProd'),
    path('categoriaprod/eliminar/<str:pk>', CategoriaProdEliminar.as_view(), name='eliminarCategoriaProd'),
    #url de categoria producto
    path('servicio/', ServicioListado.as_view(template_name="servicio/index.html"), name='leerServicio'),
    path('servicio/detalle/<str:pk>', ServicioDetalle.as_view(template_name="servicio/detalles.html"), name='detallesServicio'),
    path('servicio/crear', ServicioCrear.as_view(template_name="servicio/crear.html"), name='CrearServicio'),
    path('servicio/editar/<str:pk>', ServicioActualizar.as_view(template_name="servicio/actualizar.html"), name='actualizarServicio'),
    path('servicio/eliminar/<str:pk>', ServicioEliminar.as_view(), name='eliminarServicio'),
]

