

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
    return render(request, 'Base/base_index.html')

def registrarMeses(request):
    formMes = forms.MesesForms()
    
    if request.method == 'POST':
        formMes = forms.MesesForms(request.POST)
        if formMes.is_valid():
            formMes.save()

            # redireccion automatica
            return HttpResponseRedirect(reverse('resultados_graficos'))
    
    data = {'formKey':formMes}
    return render(request, 'Contenidos/Formulario/registrar_meses.html', data)



