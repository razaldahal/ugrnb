from . import views
from django.conf.urls import include
from django.urls import path

urlpatterns=[path('outlet',views.add_outlet,name='get_outlets'),
path('outlet/add',views.add_outlet,name='add_outlets'),
# path('outlet/<int:id>',get_outlet,name='retrieve_outlet'),
# path('outlet/<int:id>/update',add_outlet,name='update_outlet'),
# path('outlet/<int:id>/delete',delete_outlet,name='delete_outlet'),
# path('zone/add',add_zone,name='add_zones'),
# path('zone/<int:id>/update',add_zone,name='update_zone'),
# path('zone',get_zone,name='list_zones'),
# path('zone/<int:id>',get_zone,name='retrieve_zone'),
# path('zone/<int:id>/delete',delete_zone,name='delete_zone'),
# path('table/add',add_table,name='add_tables'),
# path('table/<int:id>/update',add_table,name='update_table'),
# path('table',get_table,name='list_tables'),
# path('table/<int:id>',get_table,name='retrieve_table'),
# path('table/<int:id>/delete',delete_table,name='delete_table'),
# path('seat/add',add_seat,name='add_seats'),
# path('seat/<int:id>/update',add_seat,name='update_seat'),
# path('seat',get_seat,name='list_seats'),
# path('seat/<int:id>',get_seat,name='retrieve_seat'),
# path('seat/<int:id>/delete',delete_seat,name='delete_seat')
]