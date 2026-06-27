
# '======[Importaciones]============================'
from django.db import models

# '==============================================='

# °===========================°
#    °Models -> roseApp
# °===========================°

class Mes(models.Model):
    num_mes = models.IntegerField()
    
    # VAR -> Pa
    precio_actual = models.DecimalField(max_digits=12, decimal_places=2)

    # precio anterior a la subida -> requerido para obtener la variacion
    precio_anterior = models.DecimalField(max_digits=12, decimal_places=2)
    
    # Sub totales
    sub_totales_activos = models.IntegerField()

    # VAR -> Sm
    sub_mensuales_nuevas_max = models.IntegerField()

    # VAR -> Sp
    sub_mensuales_perdidas_max = models.IntegerField()
    

    # VAR -> Up -> porcentaje estandarizado
    tasa_perdida_base = models.DecimalField(max_digits=5, decimal_places=4, default=0.02)

    def __str__(self):
        return f"Mes {self.num_mes} - Precio: {self.precio_actual}"

    """
    @property 
    Util para calcular valores en el momento con datos de la DB sin la necesidad 
    crear una variable y el metodo se llama [mes.variacion_precio] sin () y se 
    maneja como una variable. Es un metodo de solo lectura. 
    """

    # VAR -> Vps
    @property
    def variacion_precio(self):
        """Calcula la variacion del precio"""
        return self.precio_actual - self.precio_anterior

    # VAR -> Tasa F.
    @property
    def tasa_fuga(self):
        """Calcula Tasa F. de este mes solo dos meses"""
        if self.sub_totales_activos > 0:
            return self.sub_mensuales_perdidas_max / self.sub_totales_activos
        return 0



class PrediccionMes(models.Model):

    mes = models.OneToOneField(Mes, on_delete=models.CASCADE, related_name='prediccion')
    
    # VAR -> Tpn
    tasa_perdida_nuevos_no_suscritos = models.DecimalField(max_digits=15, decimal_places=6)

    # VAR -> Per
    tasa_perdida_antiguos_suscritos = models.DecimalField(max_digits=15, decimal_places=6)
    
    # VAR -> Adq()
    f_adquisicion = models.DecimalField(max_digits=15, decimal_places=4)

    # VAR -> Chr()
    f_churn = models.DecimalField(max_digits=15, decimal_places=4)
    
    # VAR -> U()
    usuarios_estables = models.IntegerField()

    # VAR -> I()
    ingresos_totales = models.DecimalField(max_digits=15, decimal_places=2)
    
    # VAR -> para la 1era derivada??
    # precio_optimo_1derivada = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # VAR -> para la 2da derivada??
    # ganancia_maxima_2derivada = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return f"Resultados óptimos - Mes {self.mes.num_mes}"











