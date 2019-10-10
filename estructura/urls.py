# estructura/urls.py
from django.urls import path

from .views import HabitacionListado, HabitacionDetalle, HabitacionCrear, HabitacionActualizar, HabitacionEliminar

urlpatterns = [
    path('', HabitacionListado.as_view(template_name = "habitacion/index.html"), name='leerHabitacion'),
    path('detalle/<str:pk>', HabitacionDetalle.as_view(template_name = "habitacion/detalles.html"), name='detalles'),
    path('crear', HabitacionCrear.as_view(template_name = "habitacion/crear.html"), name='crear'),
    path('editar/<str:pk>', HabitacionActualizar.as_view(template_name = "habitacion/actualizar.html"), name='actualizar'), 
    path('eliminar/<str:pk>', HabitacionEliminar.as_view(), name='eliminar'),
    
]

