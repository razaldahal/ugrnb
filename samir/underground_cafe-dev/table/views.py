from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse,JsonResponse
from .forms import TableForm
from .models import Table
# Create your views here.
def table(request):

	
	if request.method=='POST':

	    form=TableForm(request.POST)
	    
	    if form.is_valid:

	    	form.save()
	
	else:
		pass    	

	list_table=Table.objects.all()

	return render(request,'order/table_order.html',{'list_table':list_table,'form':TableForm()})
		

	