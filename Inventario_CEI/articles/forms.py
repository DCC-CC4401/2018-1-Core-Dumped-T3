from django import forms
from re import sub
from .models import Article

class NameEditForm(forms.Form):
  name = forms.CharField(
    label="Nuevo nombre:",
    widget=forms.TextInput(
      attrs={
        'class': 'form-control'
      }
    )
  )

  def set_name(self, placeholderString):
    '''Adds a placeholder attribute on the name's widget, and returns the object.'''
    self.fields['name'].widget.attrs.update({'placeholder': placeholderString})
    return self

class StatusEditForm(forms.Form):
  status = forms.ChoiceField(
    label="Nuevo estado:",
    choices= Article.ARTICLE_STATES,
    widget=forms.Select(
      attrs = {
        'class': 'form-control'
      }
    )
  )

  def set_choice(self, choice):
    '''Adds a placeholder attribute on the status' widget, and returns the object.'''
    self.fields['status'].widget.attrs.update({'placeholder': choice})
    return self


class ImageEditForm(forms.Form):
  image = forms.ImageField(
    label="Seleccionar imagen",
    widget=forms.FileInput(
      attrs = {
        'class': 'form-control'
      }
    )
  )

class DescriptionEditForm(forms.Form):
  description = forms.CharField(
    label="Nueva descripción.",
    widget=forms.Textarea(
      attrs = {
        'class': 'form-control'
      }
    )
  )

  def set_description(self, description):
    '''Adds a placeholder attribute on the description' widget, and returns the object.'''
    self.fields['description'].widget.attrs.update({'placeholder': description})
    return self