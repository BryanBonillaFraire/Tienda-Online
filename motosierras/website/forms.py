from django import forms
from .models import Domicilio

class DomicilioForms(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = ('nombre', 'apellido', 'telefono', 'calle1', 'calle2', 'ciudad', 'estado', 'cp', 'email')

        widgets = { 
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'calle1': forms.TextInput(attrs={'class': 'form-control'}),
            'calle2': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'cp': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }