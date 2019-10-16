from django.shortcuts import render
from django import views
from django.http.response import JsonResponse,json
from django.http import request
from django.views.decorators import csrf
from users.forms import UserForm
# Create your views here.

def register(request):
    userform=UserForm()
    return render(request,'register.html', {'form':userform})

# class UserView(views.View):    
#     def create(self,request):

#         userform = UserForm(request.POST)  
#         if userform.is_valid():  
#             try:  
#                 form.save()  
#                 return redirect('/show')  
#             except:  
#                 pass   

#         data=request.POST
#         print(data['full_name'])
#         try:
#             full_name=data['full_name']
#             address=data['address']
#             phone_no=data['phone_no']
#             email=data['email']
#             username=data['username']
#             is_staff=data['is_staff']
#             is_manager=data['is_manager']
#             is_customer=data['is_customer']
#             is_cashier=data['is_cashier']

#             a,b = User.objects.get_or_create(full_name=full_name,address=address,phone_no=phone_no,email=email,username=username,is_cashier=is_cashier,is_customer=is_customer,is_staff=is_staff,is_manager=is_manager)

#             if a.is_staff:
#                 Staff.objects.get_or_create(user=a)
#             if a.is_cashier:
#                 Cashier.objects.get_or_create(user=a)
#             if a.is_customer:
#                 Customer.objects.get_or_create(user=a)
#             if a.is_manager:
#                 Manager.objects.get_or_create(user=a)
#             if b:
#                 return JsonResponse({"Success":"Created!","username":a.username})
#             else:
#                 return JsonResponse({"Info":"This data already exists! Please choose a unique username for a new one"})                     


#         except Exception as ex:
#             return ex
    
#     def get(self,request):
        
#         all=User.objects.all()

#         for user in all:
#             if user.is_staff:
#                 text=" is a staff"
#             if user.is_cashier:
#                 text=" is a cashier"
#             if user.is_customer:
#                 text=" is a customer"
#             if user.is_manager:
#                 text=" is the manager"

#         try:
#             for user in all:
#                 return JsonResponse({"id":user.id,"user":user.username,"type":"User"+text})

#         except Exception as ex:
#             return ex
