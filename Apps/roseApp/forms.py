
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
        label="Ingrese el precio inicial de la suscripción:"
    )

    precio_anterior = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': '0.00'}),
        label="Ingrese el precio posterior al ajuste:"
    )

    sub_totales_activos = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': '0'}),
        label="Ingrese la cantidad aproximada de las suscripciones activas durante el periodo:"
    )

    sub_mensuales_nuevas_max = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': '0'}),
        label="Ingrese la cantidad total de suscripciones obtenidas durante el periodo:"
    )

    sub_mensuales_perdidas_max = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': '0'}),
        label="Ingrese la cantidad de suscripciones perdidas durante el periodo:"
    )

    # num_mes = forms.IntegerField(
    #     widget=forms.NumberInput(attrs={'class': 'form-control'}),
    #     label="Numero de mes:"
    #     )
    
    