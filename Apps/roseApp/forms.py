from django import forms
from Apps.roseApp.models import Mes

class MesesForms(forms.ModelForm):
    class Meta:
        model = Mes
        fields = '__all__'

   
    precio_actual = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label="Precio actual de la suscripcion:"
        )

    precio_anterior = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label="Precio antes del ajuste:"
        )

    sub_totales_activos = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label="Suscripciones totales (Actualmente):"
        )

    sub_mensuales_nuevas_max = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label="Suscripciones nuevas maximas (Mensuales):"
        )

    sub_mensuales_perdidas_max = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label="Suscripciones perdidas maximas (Mensuales):"
        )

    num_mes = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label="Numero de mes:"
        )
    
    