from django.shortcuts import render,render_to_response,redirect
from django import views
from .models import *
from .forms import *
from django.http.response import HttpResponse,JsonResponse
from django.template.response import TemplateResponse
from django.template.loader import render_to_string
# Create your views here.

def get_outlet(request): 
    outlets= Outlet.objects.all()
    print(outlets)
    return render(request, 'listoutlet.html', {'outlets': outlets})

def add_outlet(request):
    if request.method=='POST':
        addform=OutletForm(request.POST)
        if addform.is_valid:
            try: 
                addform.save() 
                return redirect('list_outlets') 
                 
            except: 
                print("Error")
                pass 
    else:
        addform=OutletForm()

    return render(request, 'addoutlet.html', {'form': addform})

def delete_outlet(request, id):    
    outlet = Outlet.objects.get(id=id)  
    outlet.delete()  
    return redirect('list_outlets')  

def update_outlet(request, id):
    myoutlet=Outlet.objects.get(id=id) 
    if request.method == 'POST':
        form = OutletForm(request.POST, request.FILES, instance = myoutlet)  
        if form.is_valid(): 
            form.save()  
            return redirect('list_outlets') 

    outletform=OutletForm(instance = myoutlet)
    return render(request, 'addoutlet.html', {'form':outletform})

# Views For Zone
def add_zone(request):
    if request.method=='POST':
        addform=ZoneForm(request.POST)
        if addform.is_valid:
            try: 
                addform.save() 
                return redirect('list_zones')
                 
            except: 
                print("Error")
                pass 
    else:
        print("Not post method")
        addform=ZoneForm()
    return render(request,'addzone.html',{'form':addform})

    
def get_zone(request):    
    zones= Zone.objects.all()
    return render(request, 'listzone.html', {'zones': zones})

def delete_zone(request, id):    
    zone = Zone.objects.get(id=id)  
    zone.delete()  
    return redirect("list_zones")

def update_zone(request, id):
    myzone = Zone.objects.get(id=id) 
    if request.method == 'POST':
        form = ZoneForm(request.POST, request.FILES, instance = myzone)  
        if form.is_valid(): 
            form.save()  
            return redirect('list_outlets') 

    zoneform=ZoneForm(instance = myzone)
    return render(request, 'addzone.html', {'form':zoneform})

# Table View
def get_table(request): 
    tables= Table.objects.all()
    print(tables)
    return render(request, 'listtables.html', {'tables': tables})

def add_table(request):
    if request.method=='POST':
        addform=TableForm(request.POST)
        if addform.is_valid:
            try: 
                addform.save() 
                return redirect('list_tables') 
                 
            except: 
                print("Error")
                pass 
    else:
        addform=TableForm()

    return render(request, 'addtable.html', {'form': addform})

def delete_table(request, id):    
    table = Table.objects.get(id=id)  
    table.delete()  
    return redirect("list_tables")  

def update_table(request, id):
    mytable=Table.objects.get(id=id) 
    if request.method == 'POST':
        form = TableForm(request.POST, request.FILES, instance = mytable)  
        if form.is_valid(): 
            form.save()  
            return redirect("list_tables") 

    tableform=TableForm(instance = mytable)
    return render(request, 'addtable.html', {'form':tableform})

# Views For Seat
def add_seat(request):
    if request.method=='POST':
        addform=SeatForm(request.POST)
        if addform.is_valid:
            try: 
                addform.save() 
                return redirect('list_seats') 
                 
            except: 
                print("Error")
                pass 
    else:
        print("Not post method")
        addform=SeatForm()
    return render(request,'addseat.html',{'form':addform})

    
def get_seat(request):    
    seats = Seat.objects.all()
    print(seats)
    return render(request,'listseats.html', {'seats':seats})

def delete_seat(request, id):    
    seats = Seat.objects.get(id=id)  
    seats.delete()  
    return redirect("list_seats")

def update_seat(request, id):
    myseat=Seat.objects.get(id=id) 
    if request.method == 'POST':
        form = SeatForm(request.POST, request.FILES, instance = myseat)  
        if form.is_valid(): 
            form.save()  
            return redirect("list_seats") 

    tableform=SeatForm(instance = myseat)
    return render(request, 'addtable.html', {'form':tableform})