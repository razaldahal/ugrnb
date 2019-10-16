from django.forms import ModelForm
from .models import Table
from django import forms

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('__all__')


