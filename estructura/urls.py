# estructura/urls.py
from django.urls import path

from .views import HabitacionListado, HabitacionDetalle, HabitacionCrear, HabitacionActualizar, HabitacionEliminar

urlpatterns = [
    path('habitacion/', HabitacionListado.as_view(template_name = "habitacion/index.html"), name='leerHabitacion'),
    path('habitacion/detalle/<str:pk>', HabitacionDetalle.as_view(template_name = "habitacion/detalles.html"), name='detalles'),
    path('habitacion/crear', HabitacionCrear.as_view(template_name = "habitacion/crear.html"), name='crear'),
    path('habitacion/editar/<str:pk>', HabitacionActualizar.as_view(template_name = "habitacion/actualizar.html"), name='actualizar'),
    path('habitacion/eliminar/<str:pk>', HabitacionEliminar.as_view(), name='eliminar'),

]

