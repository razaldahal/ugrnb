from django.shortcuts import render,redirect
from order.models import OrderItem
from.form import UpdateKotForm
from django import views
   
def get_kot(request):
    kots=OrderItem.objects.all()
    # print(kots)
    kot = [ ]
    for k in kots:
        kotlist= {
        'id':k.id,
        'orderby':k.orderby,
        'orderitems':k.orderitems,
        'quantity':k.quantity,
        'kotstatus':k.get_kotstatus_display()
        }
        kot.append(kotlist)

    # print(kot[0]['kotstatus'])
 
    return render(request,'listkot.html',{'orderitems':kot})

def updatekot(request,id):
    status=OrderItem.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateKotForm(request.POST, request.FILES, instance=status)
        if form.is_valid:
            form.save()
            return redirect('getkot')
    else:
        sform=UpdateKotForm(instance=status)
    return render(request, 'updatekot.html', {'form':sform})