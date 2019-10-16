from django.db import models

# Create your models here.

class User(models.Model):
    full_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    phone_no=models.CharField(max_length=255)
    email=models.EmailField(null=True)
    username=models.CharField(max_length=255,unique=True)
    is_staff=models.BooleanField(default=False)
    is_manager=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)
    is_cashier=models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
class Staff(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
class Manager(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username   
class Cashier(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)            


    def __str__(self):
        return self.user.username




