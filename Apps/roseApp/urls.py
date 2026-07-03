
# '======[Importaciones]============================'
from django.contrib import admin
from django.urls import path

from Apps.roseApp.views import *
from Apps.roseApp.views import *
# '==============================================='

# °===========================°
#    °URLs -> roseApp
# °===========================°

urlpatterns = [

    path('registrar-meses/', registrarMeses, name='registrar_meses'),

    path('proyecciones/', listadoProyecciones, name='listado_proyecciones'),

    path('proyeccion/<int:prediccion_id>/', detalleProyeccion, name='mostrar_proyeccion'),

]

