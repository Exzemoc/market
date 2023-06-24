from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_page, name='staff_orders'),
    path('confirm_order/<int:order_id>/', views.confirm_order, name='confirm_order'),
    path('close_order/<int:order_id>/', views.close_order, name='close_order'),
]