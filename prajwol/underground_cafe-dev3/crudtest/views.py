from django.shortcuts import render,redirect
from .forms import TableForm
from .models import Table

def menu(request):
    return render (request,'menu/menuitems.html')

def outlet(request):
    return render (request,'spaces/outlet.html')

def zone(request):
    return render (request,'spaces/zone.html')

def table(request):
    form=TableForm()
    if request.method == 'POST':
        form=TableForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        pass
    form = TableForm()

    table=Table.objects.all()  
    return render(request,"spaces/table.html",{'tables':table,'form':form}) 

def tableremove(request, id):  
    table = Table.objects.get(id=id)  
    table.delete()  
    return redirect("table") 

def seat(request):
    return render (request,'spaces/seat.html')

def user(request):
    return render (request,'user/user.html')

def employee(request):
    return render (request,'employee/employee.html')

def customer(request):
    return render (request,'customer/customer.html')

def stock(request):
    return render (request,'stock/stock.html')