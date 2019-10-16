from order import views
from django.conf.urls import include
from django.urls import path


urlpatterns=[
    path('menucard/add/',views.add_items,name='add_items'),
    path('menucards/',views.get_items,name='get_items'),
    path('menucard/<int:id>/update',views.update_items,name='update_items'),
    path('menucard/<int:id>/delete',views.delete_items,name='delete_items'),
    path('addorder/',views.add_order_items,name='add_orders'),
    path('orders/',views.get_order_items,name='get_orders'),
    path('order/<int:id>/delete',views.delete_order_items,name='delete_orders'),
    path('order/<int:id>/update',views.update_order_items,name='update_orders'),


]