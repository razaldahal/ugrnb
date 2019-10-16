from django.shortcuts import render,redirect
from django import views
from django.contrib import messages
from django.http.response import JsonResponse,json
from django.http import request
from django.views.decorators import csrf
from .forms import UserForm
from .models import *


def create(request): 
    if request.method=='POST':
        data=request.POST
        form=UserForm()
        form1=UserForm(data)
        if form1.is_valid():
            print(data)       
            try:
                is_staff=data.get('is_staff',False)
                is_manager=data.get('is_manager',False)
                is_customer=data.get('is_customer',False)
                is_cashier=data.get('is_cashier',False)
                
                obj = form1.save()                
                if bool(is_staff):  
                    Staff.objects.get_or_create(user=obj)                                                        
                if bool(is_cashier):
                    Cashier.objects.get_or_create(user=obj) 
                if bool(is_customer): 
                    Customer.objects.get_or_create(user=obj) 
                if bool(is_manager):
                    Manager.objects.get_or_create(user=obj) 

                messages.info(request,"User created successfully")    
                return redirect("list_users") 
   
             
            except Exception as ex:
                return JsonResponse({"Info":str(ex)})  

        else:
            print("User already exits try new one")
            messages.info(request,"User already exits try new one")
            return redirect("add_user") 
    form=UserForm()
    return render(request,'adduser.html',{'form':form})
    
def getUser(request,id=0):
    users= User.objects.all()
    return render(request, 'listuser.html', {'users': users})

def delete_user(request, id):    
    user = User.objects.get(id=id)  
    user.delete()  
    return redirect("list_users")  

def update_user(request, id):
    myuser=User.objects.get(id=id) 
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance = myuser)  
        if form.is_valid(): 
            form.save()  
            return redirect("list_users") 

    userform=UserForm(instance = myuser)
    return render(request, 'adduser.html', {'form':userform})