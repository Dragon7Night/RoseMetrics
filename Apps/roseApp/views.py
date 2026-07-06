

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

def formula(request):
    return render(request, 'Contenidos/formulas.html')

ESCALA_MONEDA = 1000

def registrarMeses(request):
    
    # for k, v in request.POST.items():
    #     print(k, "->", v)

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

            # print()

            # print("OBJETO MES ACTUAL")

            # print(mesActual.precio_anterior)
            # print(mesActual.precio_actual)

            # print()

            # print("----- OBJETO -----")
            # print(mesActual.__dict__)
            # print("------------------")

            # obtener el ultimo dia del mes de la DB y se suma 1
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

            # print("===== DATOS RECIBIDOS =====")
            # print("Precio anterior:", mesActual.precio_anterior)
            # print("Precio actual:", mesActual.precio_actual)
            # print("Suscripciones nuevas:", mesActual.sub_mensuales_nuevas_max)
            # print("Suscripciones perdidas:", mesActual.sub_mensuales_perdidas_max)
            # print("===========================")

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
            # Precio posterior del periodo actual
            Pa_actual = float(mesActual.precio_actual) / ESCALA_MONEDA

            # Precio inicial del mismo periodo
            Pa_inicial = float(mesActual.precio_anterior) / ESCALA_MONEDA

            # Variación del precio del periodo actual
            Vps = Pa_actual - Pa_inicial

            # print("--------------------------------")
            # print("Precio anterior:", Pa_inicial)
            # print("Precio actual:", Pa_actual)
            # print("Vps:", Vps)
            # print("--------------------------------")

            # Validación matemática
            if Vps <= 0:
                raise ValueError(
                    "La variación del precio debe ser mayor que cero para aplicar el modelo."
                )
            

            Sm = max(
                float(mesAnterior.sub_mensuales_nuevas_max),
                float(mesActual.sub_mensuales_nuevas_max))

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
            adq_actual = max(0,float(Adq.subs(Pa, Pa_actual)))
            chr_actual = max(0.0001,float(Chr.subs(Pa, Pa_actual)))

            u_actual = round(max(0,float(U.subs(Pa, Pa_actual))))
            
            ingresos_actual = (float(mesActual.precio_actual) * float(mesActual.sub_totales_activos))

            precio_min = Pa_inicial
            precio_max = Pa_actual + 5

            mejor_precio = Pa_actual
            mejor_ingreso = -1

            paso = 0.05
            precio = precio_min

            while precio <= precio_max:
            
                adq = max(0, Sm - (Tpn * precio))
                chr = max(0.0001, Up + (Per * precio))

                usuarios = adq / chr

                ingreso = precio * usuarios

                if ingreso > mejor_ingreso:
                    mejor_ingreso = ingreso
                    mejor_precio = precio

                precio += paso

            precio_optimo = mejor_precio

            segundaDerivada_r = 0


            # guardar datos de la nueva prediccion
            
            nueva_prediccion = models.PrediccionMes.objects.create(
                mes=mesActual, 
                tasa_perdida_nuevos_no_suscritos=Tpn,
                tasa_perdida_antiguos_suscritos=Per,
                f_adquisicion=adq_actual,
                f_churn=chr_actual,
                usuarios_estables=u_actual,
                ingresos_totales=ingresos_actual,
                precio_optimo_1derivada=precio_optimo * ESCALA_MONEDA,
                ganancia_maxima_2derivada=segundaDerivada_r
            )

            # redireccionamiento directo a la proyeccion
            return HttpResponseRedirect(reverse('mostrar_proyeccion', args=[nueva_prediccion.id]))

    else:
        # se crean los forms vacios y dividido
        formMesAnterior = forms.MesesForms(prefix='fAnterior')
        formMesActual = forms.MesesForms(prefix='fActual')
    
    
    data = {
        'formKeyAnterior':formMesAnterior,
        'formKeyActual':formMesActual,
        }
    return render(request, 'Contenidos/Formulario/registrar_meses.html', data)


def listadoProyecciones(request):
    """
    muestra todas las proyecciones registradas en la DB
    """
    predicciones = models.PrediccionMes.objects.all().order_by('-id')

    data = {'predicciones': predicciones}

    return render(request, 'Contenidos/Resultados/listado_proyecciones.html', data)



def detalleProyeccion(request, prediccion_id):
    """
    Muestra una proyeccion por ID con todos sus detalles y graficos
    """

    prediccion = get_object_or_404(models.PrediccionMes, id=prediccion_id)
    mesActual = prediccion.mes
    
    # se obtiene el mes anterior para hacer la comparacion
    mesAnterior = models.Mes.objects.filter(num_mes=mesActual.num_mes - 1).first()
    
    if mesAnterior:
        ingreso_historico = float(mesAnterior.precio_actual) * int(mesAnterior.sub_totales_activos)
        precio_historico = float(mesAnterior.precio_actual)
        subs_historicas = int(mesAnterior.sub_totales_activos)
    else:
        ingreso_historico = 0.0
        precio_historico = float(mesActual.precio_anterior)
        subs_historicas = 0

    # se re-calcula el ingreso optimo basado en los registros
    Sm = max(
        float(mesAnterior.sub_mensuales_nuevas_max),
        float(mesActual.sub_mensuales_nuevas_max))
    Up = float(mesActual.tasa_perdida_base)
    Tpn = float(prediccion.tasa_perdida_nuevos_no_suscritos)
    Per = float(prediccion.tasa_perdida_antiguos_suscritos)
    precio_optimo = (float(prediccion.precio_optimo_1derivada)/ 1000)

    adq_optimo = max(0, Sm - (Tpn * precio_optimo))

    chr_optimo = max(0.0001, Up + (Per * precio_optimo))

    u_optima = adq_optimo / chr_optimo if chr_optimo > 0 else 0
    ingreso_optimo_calculado = (precio_optimo* ESCALA_MONEDA* u_optima)

    ingreso_actual_real = (float(mesActual.precio_actual)* float(mesActual.sub_totales_activos))

    context = {
        "ingreso_historico": ingreso_historico,
        "ingreso_actual": ingreso_actual_real,
        "precio_historico": precio_historico,
        "precio_actual": float(mesActual.precio_actual),
        "subs_historicas": subs_historicas,
        "subs_actuales": int(mesActual.sub_totales_activos),
        "precio_optimo": precio_optimo * 1000,
        "adquisicion": float(prediccion.f_adquisicion),
        "churn": float(prediccion.f_churn),
        "ingreso_optimo": ingreso_optimo_calculado,
    }
    
    return render(request, "Contenidos/Resultados/detalle_proyeccion.html", context)