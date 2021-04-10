from django import forms
from .models import Figure

class FigureCreateForm(forms.ModelForm):
    class Meta:
        model = Figure
        fields = ('name','url','images','description')

class FigureEditForm(forms.ModelForm):
    class Meta:
        model = Figure
        fields = ('name','url','images','description')

