from django.shortcuts import render,render_to_response
from django import views
from .models import *
from .forms import *
from django.http.response import HttpResponse,JsonResponse
from django.template.response import TemplateResponse
from django.template.loader import render_to_string
# Create your views here.


def add_outlet(request,id=0):
    form=OutletForm()
    data=request.POST
    form1=OutletForm(data)
        
    if id!=0:
        print(id)

        try:
            a=Outlet.objects.get(id=id)
           
            a.name=data['name']
            a.full_address=data['full_address']
            a.save()
            return JsonResponse({"Success":"Updated Outlet "+a.name+"  Successfully"})
        except:
            pass


        if form1.is_valid():
            try:
                name=data['name']
                print(name)
                full_address=data['full_address']
        

                a,b=Outlet.objects.get_or_create(name=name,full_address=full_address)
                if b:
                    return JsonResponse({"Success!":"Created A New Outlet Successfilly"})
                else:
                    return JsonResponse({"Info":"The outlet already exists! Please try using a new name for the outlet"})
            except Exception as ex:
                return ex
    return render(request,'addoutlet.html',{'form':form}) 
        
# def get_outlet(request,id=0):
#     form=OutletListForm()
#     l=[]
#     if id!=0:
#         outlet=Outlet.objects.get(id=id)
#         l.append({"name":outlet.name,"full_address":outlet.full_address,"id":id})
#     else:

#         for outlet in Outlet.objects.all():
#             name=outlet.name
#             full_address=outlet.full_address
#             id=outlet.id
#             l.append({"name":name,"full_address":full_address,"id":id})
#     m=[]       
#     for o in l:    
#         r=render_to_string('listoutlet.html',{'form':OutletListForm(o)})    
#         m.append(r)
#     return HttpResponse(m)  
# def delete_outlet(request,id):
#     a=Outlet.objects.get(id=id)
#     name=a.name
#     a.delete()
#     return JsonResponse("Deleted Outlet "+name+" successfully")

# def add_zone(request,id=0):
#     form=ZoneForm()
#     data=request.POST
#     message=''
#     if id!=0:
#         try:
#             zone=Zone.objects.get(id=id)
#             zone.name=data['name']
#             zone.outlet=Outlet.objects.get(id=data['outlet'])
#             zone.description=data['description']
#             zone.save()
#         except:
#             pass 
#     else:       
#         if ZoneForm(data).is_valid():
#             try:
#                 name=data['name']
#                 outlet=data['outlet']
#                 description=data['description']

#                 a,b=Zone.objects.get_or_create(name=name,outlet=Outlet.objects.get(id=outlet),description=description)
#                 if b:
#                     message="Zone "+a.name+" successfully created"
#                 else:
#                     message="Zone "+a.name+" was not created because it already exists. Please choose a unique name to create a new zone"
#             except Exception as ex:
#                 message=str(ex)
                    
#     return render(request,'addzone.html',{'form':form,'message':message})

# def get_zone(request,id=0):
#     l=[]
#     if id!=0:
#         zone=Zone.objects.get(id=id)
#         l.append({"name":zone.name,"outlet":zone.outlet.id,"description":zone.description,"id":zone.id})
#     else:
#         all=Zone.objects.all()
#         for zone in all:
#             l.append({"name":zone.name,"outlet":zone.outlet.id,"description":zone.description,"id":zone.id})
#     m=[]
#     print(l)       
#     for o in l:    
#         r=render_to_string('addzone.html',{'form':ZoneForm(o)})    
#         m.append(r)
#     return HttpResponse(m) 

# def delete_zone(request,id):
#     try:
#         zone=Zone.objects.get(id=id)
#         name=zone.name
#         outlet=zone.outlet.name
#         zone.delete()
#         return HttpResponse("Successfully deleted zone "+name+" of outlet "+outlet)
#     except Exception as ex:
#         return HttpResponse(str(ex))
    
# def add_table(request,id=0):
#     form=TableForm()
#     data=request.POST
#     if id!=0:
#         try:
#             table=Table.objects.get(id=id)
#             table.name=data['name']
#             table.zone=Zone.objects.get(id=data['zone'])
#             table.save()
#             return HttpResponse('Some rseponse')
#         except:
#             pass
#     else:
#         try:
#             if TableForm(data).is_valid():
#                 name=data['name']
#                 zone=data['zone']
#                 a,b=Table.objects.get_or_create(name=name,zone=Zone.objects.get(id=zone))
#                 if b:
#                     return HttpResponse('Added table '+a.name+' in zone '+a.zone.name+' of outlet '+a.zone.outlet.name+' successfully')        
#                 else:
#                     return HttpResponse('Cannot add table beacause the table '+a.name+' already exists in zone '+a.zone.name+' of outlet '+a.zone.outlet.name+'. Please enter a unique table name to add new table')
#         except Exception as ex:
#             return HttpResponse(str(ex))
#     return render(request,'addtable.html',{'form':form})                
# def get_table(request,id=0):
#     l=[]
#     if id!=0:
#         try:
#             table=Table.objects.get(id=id)
#             l.append({'name':table.name,'zone':table.zone.name})
#         except:
#               pass  
#     else:
#         all=Table.objects.all()
#         for table in all:
#             l.append({'name':table.name,'zone':table.zone.name})
#     m=[]
#     for o in l:
#         r=render_to_string('listtable.html',{'form':TableForm(o)})
#         m.append(r)
#     return HttpResponse(m)            

# def delete_table(request,id):
#     try:
#         table=Table.objects.get(id=id)
#         name=table.name
#         zone=table.zone.name
#         outlet=table.zone.outlet.name
#         table.delete()
#         return HttpResponse("Deleted table "+name+' of zone '+zone+' of outlet '+outlet+' successfully.')
#     except Exception as ex:
#         return HttpResponse(str(ex))
# def add_seat(request,id=0):
#     form=SeatForm()
#     data=request.POST
#     if id!=0:
#         try:
#             seat=Seat.objects.get(id=id)
#             seat.name_or_number=data['name_or_number']
#             seat.table=Table.objects.get(id=data['table'])
#             seat.save()
#             return HttpResponse('Some rseponse')
#         except:
#             pass
#     else:
#         try:
#             if SeatForm(data).is_valid():
#                 name_or_number=data['name_or_number']
#                 table=data['table']
#                 a,b=Seat.objects.get_or_create(name_or_number=name_or_number,table=Table.objects.get(id=table))
#                 if b:
#                     return HttpResponse('Added seat '+a.name_or_number+' in table '+a.table.name+' of zone '+a.table.zone.name+' successfully')        
#                 else:
#                     return HttpResponse('Cannot add seat beacause the seat '+a.name_or_number+' already exists in table '+a.table.name+' of zone '+a.table.zone.name+'. Please enter a unique table name or number to add new seat')
#         except Exception as ex:
#             return HttpResponse(str(ex))
#     return render(request,'addseat.html',{'form':form})                
# def get_seat(request,id=0):
#     l=[]
#     if id!=0:
#         try:
#             seat=Seat.objects.get(id=id)
#             l.append({'name_or_number':seat.name_or_number,'table':seat.table.name})
#         except:
#               pass  
#     else:
#         all=Seat.objects.all()
#         for seat in all:
#             l.append({'name_or_number':seat.name_or_number,'table':seat.table.name})
#     m=[]
#     for o in l:
#         r=render_to_string('listseat.html',{'form':SeatForm(o)})
#         m.append(r)
#     return HttpResponse(m)            

# def delete_seat(request,id):
#     try:
#         seat=Seat.objects.get(id=id)
#         name_or_number=seat.name_or_number
#         table=seat.table.name
#         zone=seat.table.zone.name
#         seat.delete()
#         return HttpResponse("Deleted seat "+name_or_number+' of table '+table+' of zone '+zone+' successfully.')
#     except Exception as ex:
#         return HttpResponse(str(ex))