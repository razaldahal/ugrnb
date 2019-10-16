from django import forms
from order.models import MenuCard,OrderItem


class MenuCardForm(forms.ModelForm):
    class Meta:
        model = MenuCard
        fields = "__all__"



class OrderItemsForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = "__all__"