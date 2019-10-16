from django.conf.urls import include
from django.urls import path
from . import views
import re as r

urlpatterns=[path('', views.get, name='list_user'),
path('add',views.UserView,name='add_user'),
path('<int:id>',views.get,name="retrieve_user"),
]

