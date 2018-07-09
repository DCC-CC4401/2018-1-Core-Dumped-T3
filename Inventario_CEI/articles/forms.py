from django import forms
from re import sub

class ArticleNameChangeForm(forms.Form):
  day = forms.DateField(
    label="Día",
    widget=forms.DateInput(
      attrs={
        'class': 'form-control datetimepickerinput',
        'required': True,
        'data-target':'#day-datetime'
      }
    )
  )