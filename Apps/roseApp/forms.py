
# '======[Importaciones]============================'
from django import forms
from Apps.roseApp.models import Mes

# '==============================================='

# °===========================°
#    °Forms -> roseApp
# °===========================°

class MesesForms(forms.ModelForm):
    class Meta:
        model = Mes

        """
        se limitan los campos que mostrar en el form
        """
        fields = [
            'precio_actual', 
            'precio_anterior', 
            'sub_totales_activos', 
            'sub_mensuales_nuevas_max', 
            'sub_mensuales_perdidas_max'
        ]

   
    precio_actual = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': '0.00'}),
        label="Ingrese el precio actual de su suscripción:"
    )

    precio_anterior = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': '0.00'}),
        label="Ingrese el precio posterior al ajuste:"
    )

    sub_totales_activos = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': '0'}),
        label="Ingrese la cantidad aproximada de las suscripciones totales activas:"
    )

    sub_mensuales_nuevas_max = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': '0'}),
        label="Ingrese la cantidad de máxima de suscripciones obtenidas en el mes:"
    )

    sub_mensuales_perdidas_max = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': '0'}),
        label="SIngrese la cantidad máxima suscripciones perdidas en el mes:"
    )

    # num_mes = forms.IntegerField(
    #     widget=forms.NumberInput(attrs={'class': 'form-control'}),
    #     label="Numero de mes:"
    #     )
    
    