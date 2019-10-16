from django.conf.urls import include
from django.urls import path
from. import views
import re as r

urlpatterns=[
    path('', views.getUser, name='list_users'),
    path('add', views.create,name='add_user'),
    path('update/<int:id>', views.update_user,name='update_user'),
    path('delete/<int:id>', views.delete_user,name="delete_user"),
]

