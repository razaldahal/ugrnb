from django.db import models
from spaces.models import Table

class MenuCard(models.Model):
    items=models.CharField(max_length=255)
    quantity=models.CharField(max_length=20)
    price=models.CharField(max_length=20)


    def __str__(self):
        return self.items


class OrderItem(models.Model):
    orderby=models.ForeignKey(Table,on_delete=models.CASCADE)
    orderitems=models.ForeignKey(MenuCard,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=50)
    kotstatus=models.IntegerField(choices=((1,("pending")),(2,("pass"))),default=0)
    unitprice=models.CharField(max_length=50)
    totalprice=models.CharField(max_length=50)

    # def __str__(self):
        # return self.items