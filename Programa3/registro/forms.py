from django import forms
from registro.models import DatosUsuario

class CreateUser(forms.Form):
    DPI = forms.IntegerField(label="Ingrese su DPI:", widget=forms.NumberInput(attrs={'class':'input'}))
    name = forms.CharField(label="Ingrese sus nombres", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    lastname = forms.CharField(label="Ingrese sus apellidos", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    nickname = forms.CharField(label="Ingrese su alias", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(label= "Ingrese su correo electrónico", max_length=100, widget=forms.EmailInput(attrs={'class': 'input'}))
    date  = forms.DateField(label = "Ingrese su fecha de nacimiento", widget=forms.DateInput(attrs={'class': 'input'}))