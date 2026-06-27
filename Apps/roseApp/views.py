

# '======[Importaciones]============================'
from django.shortcuts import render, get_object_or_404

# ----[REDIRECCIONAMIENTO]-------------------
from django.http import HttpResponseRedirect
from django.urls import reverse

# ----[MODELS & FORMS IMPORTS]-------------------
from Apps.roseApp import models
from Apps.roseApp import forms

# ----[MATEMATICAS]-------------------
import sympy as sp
# '================================================='

# °===========================°
#    °Vistas -> roseApp
# °===========================°

# Landig page (home)
def landingPage(request):
    return render(request, 'index.html')

def registrarMeses(request):
    formMes = forms.MesesForms()
    
    if request.method == 'POST':

        """
        prefix
        esta tag sirve para establecer dos forms diferentes, por lo tanto presentar
        dos formularios para que complete el usario.
        """
        formMesAnterior = forms.MesesForms(request.POST, prefix='fAnterior')
        formMesActual = forms.MesesForms(request.POST, prefix='fActual')

        if formMesAnterior.is_valid() and formMesActual.is_valid():
            # formMesAnterior.save()
            # formMesActual.save()
            # # redireccion automatica
            # return HttpResponseRedirect(reverse('resultados_graficos'))
            pass
    else:
        # se crean los forms vacios y dividido
        formMesAnterior = forms.MesesForms(prefix='fAnterior')
        formMesActual = forms.MesesForms(prefix='fActual')
    
    
    data = {
        'formKeyAnterior':formMesAnterior,
        'formKeyActual':formMesActual,
        }
    return render(request, 'Contenidos/Formulario/registrar_meses.html', data)



