# forms.py
from django import forms
from .models import Tipo

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['id_tipo','cargo']
        labels = {
            'id_tipo': 'ID',
            'cargo': 'Nombre del Cargo'
        }
