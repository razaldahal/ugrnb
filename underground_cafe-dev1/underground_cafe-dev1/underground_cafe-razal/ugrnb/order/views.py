from django.shortcuts import render,redirect,render_to_response
from django import views
from .form import *
from order.models import MenuCard
from django.template.loader import render_to_string
from django.http.response import HttpResponse,JsonResponse
from django.template.response import TemplateResponse

def add_items(request):
    if request.method=='POST':
        additemform=MenuCardForm(request.POST)
        if additemform.is_valid:
            try:
                additemform.save()
                return redirect('get_items')
            except:
                print('error')
                pass
    else:
        additemform=MenuCardForm()

    return render(request,'additems.html',{'form':additemform})


def get_items(request):
    item=MenuCard.objects.all()
    return render(request, 'listitems.html', {'items':item})    


def update_items(request,id):
    mymenu = MenuCard.objects.get(id=id)
    if request.method == 'POST':
        form = MenuCardForm(request.POST, request.FILES, instance=mymenu)
        if form.is_valid:
            form.save()
            return redirect ("get_items")
            
    menuform=MenuCardForm(instance=mymenu)
    return render(request, 'additems.html', {'form':menuform})

def delete_items(request, id):
    items = MenuCard.objects.get(id=id)
    items.delete()
    return redirect('get_items')
    

def add_order_items(request):
    if request.method == 'POST':
        addorderitem=OrderItemsForm(request.POST)
        if addorderitem.is_valid:
            try:
                addorderitem.save()
                return redirect('get_orders')
            except:
                pass
    else:
        addorderitem=OrderItemsForm()
    return render(request, 'addorders.html', {'form':addorderitem})   


def get_order_items(request):
    order=OrderItem.objects.all()
    return render(request,'listorder.html',{'orderitems':order})

def delete_order_items(request,id):
    order=OrderItem.objects.get(id=id)
    order.delete()
    return redirect('get_orders')

def update_order_items(request,id):
    myorder=OrderItem.objects.get(id=id)
    if request.method == 'POST':
        updateorder=OrderItemsForm(request.POST,request.FILES,instance=myorder)
        if updateorder.is_valid:
            updateorder.save()
            return redirect('get_orders')
    
    orderitem=OrderItemsForm(instance=myorder)
    return render(request,'addorders.html',{'form':orderitem})