# forms.py
from django import forms
from .models import Tipo, Persona, Usuario

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['id_tipo','cargo']
        labels = {
            'id_tipo': 'ID',
            'cargo': 'Nombre del Cargo'
        }

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ["id_persona", "nombre", "apellido"]
        widgets = {
            "id_persona": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["id_persona", "id_tipo", "usuario", "pass_field"]
        widgets = {
            "id_persona": forms.Select(attrs={"class": "form-control"}),
            "id_tipo": forms.Select(attrs={"class": "form-control"}),
            "usuario": forms.TextInput(attrs={"class": "form-control"}),
            "pass_field": forms.PasswordInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["id_persona"].widget.attrs["readonly"] = "readonly"
            self.fields["id_tipo"].widget.attrs["readonly"] = "readonly"