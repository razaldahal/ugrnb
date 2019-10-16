from django.urls import path
from KOT import views


urlpatterns=[
    path('kot/',views.get_kot,name='getkot'),
    path('update/<int:id>/kot' ,views.updatekot ,name='updatekot'),
]