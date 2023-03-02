from django.forms import ModelForm
from .models import DirrecionesEnvios


class DireccionesForm(ModelForm):
    class Meta:
        model = DirrecionesEnvios
        fields = [
            'direccion', 'localidad', 'barrio'
        ]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['direccion'].widget.attrs.update({
            'class': 'form-control'
        })
