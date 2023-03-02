from django import forms
from .models import Pqr

class PqrForm(forms.ModelForm):
    class Meta:
        model = Pqr
        fields = ["titulo", "descripcion"]