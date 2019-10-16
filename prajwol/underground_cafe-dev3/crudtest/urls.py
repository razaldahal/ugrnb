from django.urls import path
from .views import *


urlpatterns=[

path('menu/',menu,name='menu'),
path('outlet/',outlet,name='outlet'),
path('zone/',zone,name='zone'),
path('table',table,name='table'),
path('table/<int:id>',tableremove,name='tabledelete'),
path('seat/',seat,name='seat'),
path('user/',user,name='user'),
path('customer/',customer,name='customer'),
path('stock/',stock,name='stock'),
path('employee/',employee,name='employee'),
]