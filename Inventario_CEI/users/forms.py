from django import forms
from re import sub

from .fields import RutField
from .models import RegisteredUser

class LoginForm(forms.Form):
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class CreateAccountForm(forms.Form):
    first_name = forms.CharField(label="Nombre", max_length=30)
    last_name = forms.CharField(label="Apellido", max_length=30)
    email = forms.EmailField(label="Email")
    username = RutField(label="Rut", max_length=12)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

