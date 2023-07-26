from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_page, name='staff_orders'),
    path('courier_orders/', views.courier_page, name='courier_orders'),
    path('confirm_order/<int:order_id>/', views.confirm_order, name='confirm_order'),
    path('close_order/<int:order_id>/', views.close_order, name='close_order'),
    path('add_product/', views.create_product, name='add_product'),
    path('delete_product/', views.delete_products_list, name='delete_product_list'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('accept_delivery/<int:order_id>/', views.accept_delivery, name='accept_delivery'),
    path('close_delivery/<int:order_id>/', views.close_delivery, name='close_delivery'),
]