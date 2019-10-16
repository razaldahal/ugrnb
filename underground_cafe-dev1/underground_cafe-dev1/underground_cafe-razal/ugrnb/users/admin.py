from django.contrib import admin
from .models import User,Staff,Manager,Customer,Cashier
# admin.site.register(User)
admin.site.register(Staff)
admin.site.register(Manager)
admin.site.register(Customer)
admin.site.register(Cashier)
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'address','username','email')
    search_fields = ['username']
admin.site.register(User, UserAdmin)
