
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

    path('resultados/', resultados, name='resultados'),

    # muestra las proyecciones en la DB
    path('proyecciones/', listadoProyecciones, name='listado_proyecciones'),
    
    # muestra las graficas por ID de la proyeccion
    path('resultados/<int:prediccion_id>/', resultadosDetalle, name='ver_resultados'),

]

