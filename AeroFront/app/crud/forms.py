from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#demo
class CustomUserCreationFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']



class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario", required=True)
    password = forms.CharField(label="Contraseña", required=True)

class Usuario(forms.Form):
    
    nombre = forms.CharField(label="Nombre")
    apellido = forms.CharField(label="Apellido")
    email = forms.CharField(label="email")
    username = forms.CharField(label="Usuario", required=True)
    password = forms.CharField(label="Contraseña", required=True)

class Avion(forms.Form):
    matricula = forms.CharField(label="Matricula", required=True)
    marca = forms.CharField(label="Marca", required=True)
    modelo = forms.CharField(label="modelo", required=True)

class Vuelo(forms.Form):
    apellido = forms.CharField(label='apellido')
    nombre = forms.CharField(label='nombre')
    matricula= forms.CharField(label='matricula')
    inicio= forms.DateTimeField(label='inicio')
    fin= forms.DateTimeField(label='fin')
    origen= forms.CharField(label='origen')
    destino= forms.CharField(label='fin')
    tiempoVuelo = forms.FloatField(label='tiempoVuelo')
    
class Uploads(forms.Form):
    nombre: forms.CharField(label='nombre')
    

    






