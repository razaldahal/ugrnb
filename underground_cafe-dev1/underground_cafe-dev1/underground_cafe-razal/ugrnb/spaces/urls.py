from . import views
from django.conf.urls import include
from django.urls import path

urlpatterns=[
    path('outlets/',views.get_outlet,name='list_outlets'),
    path('outlet/add',views.add_outlet,name='add_outlet'),
    path('outlet/<int:id>/update',views.update_outlet,name='update_outlet'),
    path('outlet/<int:id>/delete',views.delete_outlet,name='delete_outlet'),
    path('zone/add',views.add_zone, name='add_zone'),
    path('zone/<int:id>/update',views.update_zone,name='update_zone'),
    path('zones',views.get_zone,name='list_zones'),
    path('zone/<int:id>/delete',views.delete_zone,name='delete_zone'),
    path('table/add',views.add_table, name='add_table'),
    path('table/<int:id>/update',views.update_table,name='update_table'),
    path('tables',views.get_table,name='list_tables'),
    path('table/<int:id>/delete',views.delete_table,name='delete_table'),
    path('seat/add',views.add_seat, name='add_seat'),
    path('seat/<int:id>/update',views.update_seat,name='update_seat'),
    path('seats/',views.get_seat,name='list_seats'),
    path('seat/<int:id>/delete',views.delete_seat,name='delete_seat')

]