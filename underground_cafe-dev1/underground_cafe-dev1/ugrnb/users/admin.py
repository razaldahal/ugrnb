from django.contrib import admin
from .models import User,Staff,Manager,Customer,Cashier
admin.site.register(User)
admin.site.register(Staff)
admin.site.register(Manager)
admin.site.register(Customer)
admin.site.register(Cashier)
# Register your models here.
