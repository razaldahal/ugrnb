from django import forms
from  users.models import User,Customer,Staff,Manager,Cashier

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class  CustomerForm(forms.ModelForm):
    class meta:
        model = Customer
        fields ="__all__"

class  StaffForm(forms.ModelForm):
    class meta:
        model = Staff
        fields ="__all__"

class  ManagerForm(forms.ModelForm):
    class meta:
        model = Manager
        fields ="__all__"

class  CashierForm(forms.ModelForm):
    class meta:
        model = Cashier
        fields ="__all__"
