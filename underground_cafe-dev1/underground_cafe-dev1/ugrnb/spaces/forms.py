from django import forms
from spaces.models import Outlet

class OutletForm(forms.ModelForm):
    class Meta:
        model = Outlet
        fields="__all__"