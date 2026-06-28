

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

            # se crea el form guardado, pero PAUSADO para evitar ingresarlo a la DB todabia
            mesAnterior = formMesAnterior.save(commit=False)
            mesActual = formMesActual.save(commit=False)

            # obtenemos el ultimo dia del mes de la DB y le sumamos uno
            ultimoMes = models.Mes.objects.all().order_by('-num_mes').first()

            """
            operador ternario

            tras la recoleccion del numero sacado de la DB en la var [ultimo_mes] se escoje valor 
            del campo num_mes registrado en la DB

            a esta variable se le suma el numero [1] en (ultimo_mes.num_mes + 1)

            en caso se que exista un numero en la DB sigue la operacion con normalidad (if ultimo_mes)

            de caso contrario (else 1) a la variable [siguiente_num] se le asigna el numero [1]
            """
            siguienteNum = ultimoMes.num_mes + 1 if ultimoMes else 1

            # asignacion de nuemeros y suma del mes actual
            mesAnterior.num_mes = siguienteNum
            mesActual.num_mes = siguienteNum + 1

            # finalmente se guardan los formularios con los realizados
            mesAnterior.save()
            mesActual.save()

            # -------------[FUNCION MATEMATICA]---------------------------

            """
            PARA ESTE CALCULO DE LAS FUNCIONES SOLO SE CONSIDERAN LOS DATOS
            DEL MES ACTUAL (periodo actual) YA QUE EL MES ANTERIOR 
            (periodo historico) SE USA PARA 
            OBTENER LA VARIACION DEL PRECIO HISTORICO
            TASA DE PERDIDA DE SUSCRIPCIONES HISTORICO
            """

            # DEFINICION DE VARIABLES

            # precio actual (mes actual)
            Pa_actual = float(mesActual.precio_actual)

           # precio actual (mes anterior)
            Pa_anterior = float(mesAnterior.precio_actual)

            # variacion del precios actual (con validacion para evitar division por 0)
            Vps = Pa_actual - Pa_anterior
            if Vps == 0:
                Vps = 1.0  
            
            # suscripciones totales del periodo
            Sm = float(mesActual.sub_mensuales_nuevas_max)

            # suscripciones perdidas durante el periodo
            Sp = float(mesActual.sub_mensuales_perdidas_max)

            # tasa de perdida de suscripciones (sin tener un cambio en precios)
            # ESTANDAR DEFINIDO POR EMPRESAS RELACIONADAS A LA ECONOMIA -> 2%
            Up = float(mesActual.tasa_perdida_base)


            # variables de subs perdidos vs totales activos (tasa de fuja)

            # periodo ANTERIOR
            subPerdidasAnterior = mesAnterior.sub_mensuales_perdidas_max
            subTotalesAnterior = mesAnterior.sub_totales_activos

            # periodo ACTUAL
            subPerdidasActual = mesActual.sub_mensuales_perdidas_max
            subTotalesActual = mesActual.sub_totales_activos

            # tasa de fuga de suscripciones historica
            tfAnterior = float(subPerdidasAnterior) / float(subTotalesAnterior) if subTotalesAnterior > 0 else 0
            tfActual = float(subPerdidasActual) / float(subTotalesActual) if subTotalesActual > 0 else 0
            
            # variacion de la tasa de fuga historica de suscripciones
            Vtf = tfActual - tfAnterior

            # tasa de perdida de suscripciones nuevas
            Tpn = Sp / Vps

            # porcentaje de la tasa de perdida de suscripciones
            Per = Vtf / Vps

            # declarar la var 'Pa' para usarla en las ecuaciones, es como 
            # definir la 'x' en las ecuaciones (con valor variables)
            Pa = sp.Symbol('Pa')
            
            # funcion de adquisicion
            Adq = Sm - (Tpn * Pa)

            # funcion de tasa de perdida (Churn)
            Chr = Up + (Per * Pa)

            # funcion de usuarios estables
            U = Adq / Chr

            # funcion de ingreso
            I = Pa * U

            """
            .subs
            es un metodo de sympy para sustituir el valor de precio actual 
            en donde el valor de las variable [Pa_actual] se asigna a la 
            variable [Pa]

            esto se hace con todas las funciones creadas antes
            """
            adq_actual = float(Adq.subs(Pa, Pa_actual))
            chr_actual = float(Chr.subs(Pa, Pa_actual))
            u_actual = int(U.subs(Pa, Pa_actual))
            ingresos_actual = float(I.subs(Pa, Pa_actual))

            # calcular la primera derivada
            primeraD_fIngreso = sp.diff(I, Pa)

            # calcular la primera derivada igual a cero
            primeraD_igualCero = sp.solve(primeraD_fIngreso, Pa)
            
            # Filtramos para quedarnos con el precio real y positivo
            precios_viables = [float(sol) for sol in primeraD_igualCero if sol.is_real and sol > 0]
            precio_optimo = precios_viables[0] if precios_viables else Pa_actual

            """
            la segunda derivada se obtiene por orden, que si calcula la primera derivada
            la segunda derivada deriva la segunda derivada
            """

            # calcular la segunta derivada
            segundaD_fIngreso = sp.diff(primeraD_fIngreso, Pa)

            segundaDerivada_r = float(segundaD_fIngreso.subs(Pa, precio_optimo))

            # guardar datos
            
            models.PrediccionMes.objects.create(
                mes=mesActual, # mes de control
                tasa_perdida_nuevos_no_suscritos=Tpn,
                tasa_perdida_antiguos_suscritos=Per,
                f_adquisicion=adq_actual,
                f_churn=chr_actual,
                usuarios_estables=u_actual,
                ingresos_totales=ingresos_actual,


                precio_optimo_1derivada=precio_optimo, 
                confirmacion_2derivada=segundaDerivada_r
            )


            # return HttpResponseRedirect(reverse('resultados_graficos', kwargs={'mes_id': mes_actual.id}))

            return HttpResponseRedirect(request.path)


    else:
        # se crean los forms vacios y dividido
        formMesAnterior = forms.MesesForms(prefix='fAnterior')
        formMesActual = forms.MesesForms(prefix='fActual')
    
    
    data = {
        'formKeyAnterior':formMesAnterior,
        'formKeyActual':formMesActual,
        }
    return render(request, 'Contenidos/Formulario/registrar_meses.html', data)



