from django.shortcuts import render
from django import views
from django.http.response import JsonResponse,json
from django.http import request
from django.views.decorators import csrf
from users.forms import UserForm

# Create your views here.
from .forms import UserForm

def register  (request):
    pass
    
class UserView(views.View):

    
    def create(self,request):
        data=request.POST
        print(data['full_name'])
        
        
        try:
            full_name=data['full_name']
            address=data['address']
            phone_no=data['phone_no']
            email=data['email']
            username=data['username']
            is_staff=data.get('is_staff',False)
            is_manager=data.get('is_manager',False)
            is_customer=data.get('is_customer',False)
            is_cashier=data.get('is_cashier',False)

            a,b = User.objects.get_or_create(full_name=full_name,address=address,phone_no=phone_no,email=email,username=username,is_cashier=bool(is_cashier),is_customer=bool(is_customer),is_staff=bool(is_staff),is_manager=bool(is_manager))

            if a.is_staff==True:
                Staff.objects.get_or_create(user=a)
            if a.is_cashier==True:
                Cashier.objects.get_or_create(user=a)
            if a.is_customer==True: 
                Customer.objects.get_or_create(user=a)
            if a.is_manager==True:
                Manager.objects.get_or_create(user=a)
            if b:
                return JsonResponse({"Success":"Created!","username":a.username})
            else:
                return JsonResponse({"Info":"This data already exists! Please choose a unique username for a new one"})                     


        except Exception as ex:
            return ex
        return render(request,'adduser.html',{'form':form})
def get(request,id=0):
    def get_user_type(user):
        if user.is_staff:
            text=" is a staff"
        if user.is_cashier:
            text=" is a cashier"
        if user.is_customer:
            text=" is a customer"
        if user.is_manager:
            text=" is the manager"
        return text  
    if id != 0:
        user=User.objects.get(id=id)
  
        return JsonResponse({"username":user.username,"email":user.email,"phone_no":user.phone_no,"full_name":user.full_name,"type":"User"+get_user_type(user)}) 
    
    all=User.objects.all()  
    l=[]
    try:
        
        for user in all:

            d={"id":user.id,"user":user.username,"type":"User"+get_user_type(user)}
            l.append(d)

    except Exception as ex:
        return ex




