from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from usuario.models import User
from django.contrib.auth.forms import  UserChangeForm



class UserRegistroForm(UserCreationForm):
    email = forms.EmailField
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text = {k:"" for k in fields }

class UsuarioActualizar(forms.ModelForm):
    class Meta:
        user = User
        fields = ['first_name']


class EditUserProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter uour username"}))
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ingrese su primer nombre"}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ingrese su segundo nombre"}))

    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ingrese su Username"}))
    
    primer_apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ingrese su primer apellido"}))
    
    segundo_apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ingrese su segundo apellido"}))

    telefono = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Enter su telefono"}))

    opciones_tipo_doc = [('T.I', 'Tarjeta de identidad'), ('C.C', 'Cédula de ciudadanía')]

    tipoDoc = forms.ChoiceField(choices=opciones_tipo_doc, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': "Ingrese SU TIPO DE DOCUMENTO"}))
 

    class Meta:
        model = User
        fields = ['username', 'first_name', "last_name", 'email','primer_apellido','segundo_apellido','telefono','tipoDoc',]
