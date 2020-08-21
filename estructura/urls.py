# estructura/urls.py
from django.urls import path

from estructura import models
from estructura.views import HabitacionCrear, HabitacionActualizar, HabitacionEliminar
from estructura.views import ProveedorCrear, ProveedorActualizar, ProveedorEliminar
from estructura.views import ProductoCrear, ProductoActualizar, ProductoEliminar
from estructura.views import CategoriaHabCrear, CategoriaHabActualizar, CategoriaHabEliminar 
from estructura.views import CategoriaProdCrear, CategoriaProdActualizar, CategoriaProdEliminar
from estructura.views import ServicioCrear, ServicioActualizar, ServicioEliminar
from estructura.views import DispositivoCrear, DispositivoActualizar, DispositivoEliminar, Tablero, ObjetoListado, ObjetoDetalle

urlpatterns = [
    path('habitacion/', ObjetoListado.as_view(model = models.Habitacion, template_name="habitacion/index.html"), name='leerHabitacion'),
    
    path('habitacion/detalle/<str:pk>', ObjetoDetalle.as_view(model = models.Habitacion,
                                                              template_name="habitacion/detalles.html",
                                                              ), name='detallesHabitacion'),
    
    path('habitacion/crear', HabitacionCrear.as_view(template_name="crud/crear_editar.html",
                                                     extra_context={'titulo':'Crear Habitación'}), name='crearHabitacion'),
    
    path('habitacion/editar/<str:pk>', HabitacionActualizar.as_view(template_name="crud/crear_editar.html",
                                                                    extra_context={'titulo':'Editar Habitación'}), name='actualizarHabitacion'),
    
    path('habitacion/eliminar/<str:pk>', HabitacionEliminar.as_view(), name='eliminarHabitacion'),
    
    #url de Proveedor
    path('proveedor/', ObjetoListado.as_view(model = models.Proveedor,
                                             template_name="proveedor/index.html",
                                             extra_context={'titulo':'Proveedor',
                                                            'plural':'Proveedores'}), name='leerProveedor'),
    
    path('proveedor/detalle/<str:pk>', ObjetoDetalle.as_view(model = models.Proveedor, 
                                                             template_name="proveedor/detalles.html"
                                                             ), name='detallesProveedor'),
    
    path('proveedor/crear', ProveedorCrear.as_view(template_name="crud/crear_editar.html",
                                                   extra_context={'titulo':'Crear Proveedor'}), name='crearProveedor'),
    
    path('proveedor/editar/<str:pk>', ProveedorActualizar.as_view(template_name="crud/crear_editar.html",
                                                                  extra_context={'titulo':'Editar Proveedor'}), name='actualizarProveedor'),
    
    path('proveedor/eliminar/<str:pk>', ProveedorEliminar.as_view(), name='eliminarProveedor'),
    
    #url de Producto
    path('producto/', ObjetoListado.as_view(model = models.Producto,
                                            template_name="producto/index.html",
                                            extra_context={'titulo':'Producto',
                                                           'plural':'Productos'}), name='leerProducto'),
    
    path('producto/detalle/<str:pk>', ObjetoDetalle.as_view(model = models.Producto,
                                                            template_name="producto/detalles.html",
                                                            ), name='detallesProducto'),
    
    path('producto/crear', ProductoCrear.as_view(template_name="crud/crear_editar.html",
                                                 extra_context={'titulo':'Crear Producto'}), name='CrearProducto'),
    
    path('producto/editar/<str:pk>', ProductoActualizar.as_view(template_name="crud/crear_editar.html",
                                                                extra_context={'titulo':'Editar Producto'}), name='actualizarProducto'),
    
    path('producto/eliminar/<str:pk>', ProductoEliminar.as_view(), name='eliminarProducto'),
    
    #url de categoria habitacion
    path('categoriahab/', ObjetoListado.as_view(model = models.CategoriaHab, 
                                                template_name="categoriahab/index.html", 
                                                extra_context={'titulo':'Categoría de Habitación',
                                                               'plural':'Categorías de Habitaciones'}), name='leerCategoriaHab'),
    
    path('categoriahab/detalle/<str:pk>', ObjetoDetalle.as_view(model = models.CategoriaHab,
                                                                template_name="categoriahab/detalles.html",
                                                                ), name='detallesCategoriaHab'),
    
    path('categoriahab/crear', CategoriaHabCrear.as_view(template_name="crud/crear_editar.html",
                                                         extra_context={'titulo':'Crear Categoría de Habitación'}), name='CrearCategoriaHab'),
    
    path('categoriahab/editar/<str:pk>', CategoriaHabActualizar.as_view(template_name="crud/crear_editar.html",
                                                                        extra_context={'titulo':'Editar Categoría de Habitación'}), name='actualizarCategoriaHab'),
    
    path('categoriahab/eliminar/<str:pk>', CategoriaHabEliminar.as_view(), name='eliminarCategoriaHab'),
    
    #url de categoria producto
    path('categoriaprod/', ObjetoListado.as_view(model = models.CategoriaProd,
                                                 template_name="categoriaprod/index.html",
                                                 extra_context={'titulo':'Categoría de Producto',
                                                                'plural':'Categorías de Productos'}), name='leerCategoriaProd'),
    
    path('categoriaprod/detalle/<str:pk>', ObjetoDetalle.as_view(model = models.CategoriaProd, 
                                                                 template_name="categoriaprod/detalles.html",
                                                                 ), name='detallesCategoriaProd'),
    
    path('categoriaprod/crear', CategoriaProdCrear.as_view(template_name="crud/crear_editar.html",
                                                           extra_context={'titulo':'Crear Categoría de Producto'}), name='CrearCategoriaProd'),
    
    path('categoriaprod/editar/<str:pk>', CategoriaProdActualizar.as_view(template_name="crud/crear_editar.html",
                                                                          extra_context={'titulo':'Editar Categoría de Producto'}), name='actualizarCategoriaProd'),
    
    path('categoriaprod/eliminar/<str:pk>', CategoriaProdEliminar.as_view(), name='eliminarCategoriaProd'),
    
    #url de servicio
    path('servicio/', ObjetoListado.as_view(model = models.Servicio,
                                            template_name="servicio/index.html",
                                            extra_context={'titulo':'Servicio',
                                                           'plural':'Servicios'}), name='leerServicio'),
    
    path('servicio/detalle/<str:pk>', ObjetoDetalle.as_view(model = models.Servicio,
                                                            template_name="servicio/detalles.html",
                                                            ), name='detallesServicio'),
    
    path('servicio/crear', ServicioCrear.as_view(template_name="crud/crear_editar.html",
                                                 extra_context={'titulo':'Crear Servicio'}), name='CrearServicio'),
    
    path('servicio/editar/<str:pk>', ServicioActualizar.as_view(template_name="crud/crear_editar.html",
                                                                extra_context={'titulo':'Editar Servicio'}), name='actualizarServicio'),
    
    path('servicio/eliminar/<str:pk>', ServicioEliminar.as_view(), name='eliminarServicio'),
    
    #url de dispositivo
    path('dispositivo/', ObjetoListado.as_view(model = models.Dispositivo,
                                               template_name="dispositivo/index.html",
                                               extra_context={'titulo':'Dispositivo',
                                                              'plural':'Dispositivos'}), name='leerDispositivo'),
    
    path('dispositivo/detalle/<str:pk>', ObjetoDetalle.as_view(model = models.Dispositivo,
                                                               template_name="dispositivo/detalles.html",
                                                               ), name='detallesDispositivo'),
    
    path('dispositivo/crear', DispositivoCrear.as_view(template_name="crud/crear_editar.html",
                                                       extra_context={'titulo':'Crear Dispositivo'}), name='CrearDispositivo'),
    
    path('dispositivo/editar/<str:pk>', DispositivoActualizar.as_view(template_name="crud/crear_editar.html",
                                                                      extra_context={'titulo':'Editar Dispositivo'}), name='actualizarDispositivo'),
    
    path('dispositivo/eliminar/<str:pk>', DispositivoEliminar.as_view(), name='eliminarDispositivo'),
    path('dispositivo/tablero', Tablero.as_view(template_name="dispositivo/monitor.html"), name='tablero'),

]

