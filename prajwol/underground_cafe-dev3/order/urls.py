from django.urls import path
from django.conf.urls import include
from .views import table_order

urlpatterns=[

path('',table_order,name='table_order'),


]