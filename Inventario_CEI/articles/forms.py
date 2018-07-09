from django import forms
from re import sub

class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = '__all__'
    labels = {
      'name': "Cambiar nombre:",
      'status': "Cambiar estado:",
      'image': "Seleccionar imagen",
      'description': "Cambiar descripción"
    }
    widgets = {
      'name': forms.TextInput(
        attrs = {
          'class': 'form-control'
        }
      ),
      'status': forms.Select(
        attrs = {
          'class': 'form-control'
        }
      ),
      'image': forms.FileInput(
        attrs = {
          'class': 'form-control'
        }
      ),
      'description': forms.Textarea(
        attrs = {
          'class': 'form-control'
        }
      )
    }
