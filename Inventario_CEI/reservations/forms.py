from django import forms

from .models import ArticleReservation

class ArticleReservationForm(forms.ModelForm):
    class Meta:
        model = ArticleReservation
        fields = ["initial_date", "end_date"]