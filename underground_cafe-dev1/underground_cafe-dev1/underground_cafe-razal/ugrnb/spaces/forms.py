from django import forms
from spaces.models import Outlet, Zone, Table, Seat

class OutletForm(forms.ModelForm):
    class Meta:
        model = Outlet    
        fields = '__all__'

class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone    
        fields = '__all__'

class TableForm(forms.ModelForm):
    class Meta:
        model = Table    
        fields = '__all__'

class SeatForm(forms.ModelForm):
    class Meta:
        model = Seat    
        fields = '__all__'
