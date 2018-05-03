from django import forms
from django.core.files.images import get_image_dimensions

from .models import RegisteredUser

class LoginForm(forms.Form):
    rut = forms.CharField(label="RUT", max_length=12)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
