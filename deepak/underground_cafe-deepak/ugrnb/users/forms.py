from django import forms
from users.models import User, Customer, Staff, Manager, Cashier

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"

class CashierForm(forms.ModelForm):
    class Meta:
        model = Cashier
        fields = "__all__"

class ManagerrForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = "__all__"