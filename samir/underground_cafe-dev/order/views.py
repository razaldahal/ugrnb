from django.shortcuts import render,redirect



# Create your views here.
def table_order(request):
    return render(request,'order/table_order.html')