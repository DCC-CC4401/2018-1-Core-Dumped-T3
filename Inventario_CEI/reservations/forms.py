from django import forms
from re import sub

from .models import RegisteredUser

class ReservationForm(forms.Form):
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
    start_time = forms.TimeField(
      label="Desde",
      widget=forms.TimeInput(
        attrs={
          'class': 'form-control datetimepickerinput',
          'required': True,
          'data-target':'#initial-datetime'
        }
      )
    )
    end_time = forms.TimeField(
      label="Hasta",
      widget=forms.TimeInput(
        attrs={
          'class': 'form-control datetimepickerinput',
          'required': True,
          'data-target':'#end-datetime'
        }
      )
    )

    # <input type="text" name="day" class="form-control datetimepicker-input" required data-target="#day-datetime"/>
