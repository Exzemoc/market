from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment_view, name='payment'),
    path('', views.cart_view, name='cart'),
]
