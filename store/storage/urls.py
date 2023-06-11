from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('<int:pk>/', views.product_detail, name='product_room'),
    path('rate_product/<int:pk>/', views.rate_product, name='rate_product'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
]

