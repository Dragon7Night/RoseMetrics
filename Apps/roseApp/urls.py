from django.contrib import admin
from django.urls import path

# IMPORTACION DE LAS VIEWS DE LA APP
from Apps.roseApp.views import *

urlpatterns = [

    # URLS de Estado -- CRUD de Django
    # path('data-estado/', dataEstado, name='data_estado'),
    # path('registrar-estado/', registrarEstado, name='registrar_estado'),
    # path('editar-estado/<int:id_estado>', editarEstado, name='editar_estado'),
    # path('eliminar-estado/<int:id_estado>', eliminarEstado, name='eliminar_estado'),

    # # URLS de Reserva -- CRUD de Django
    # path('data-reserva/', dataReserva, name='data_reserva'),
    # path('registrar-reserva/', registrarReserva, name='registrar_reserva'),
    # path('editar-reserva/<int:id_reserva>', editarReserva, name='editar_reserva'),
    # path('eliminar-reserva/<int:id_reserva>', eliminarReserva, name='eliminar_reserva'),

    # # URLS de Estado -- CRUD de la Api
    # path('data-estado-api/', estadoDataApi, name='data_estado_api'),
    # path('crud-estado-api/<int:pk>', estadoCrudApi, name='crud_estado_api'),

    # # URLS de Reserva -- CRUD de la Api
    # path('data-reserva-api/', reservaDataApi, name='data_reserva_api'),
    # path('crud-reserva-api/<int:pk>', reservaCrudApi, name='crud_reserva_api'),
]





