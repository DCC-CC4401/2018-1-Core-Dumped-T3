from django.contrib.auth.forms import PasswordChangeForm
from django import forms


class FormChangePassword(PasswordChangeForm):

    new_password1 = forms.CharField(label="Nueva contraseña",widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Confirmar nueva contraseña", widget=forms.PasswordInput)
    old_password = forms.CharField(label="Contraseña actual", widget=forms.PasswordInput)

