from django import forms
from order.models import OrderItem
from order.form import OrderItemsForm


class UpdateKotForm(OrderItemsForm):
    class Meta:
        model = OrderItem
        fields = ('kotstatus',)
