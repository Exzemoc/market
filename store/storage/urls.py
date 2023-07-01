from django.urls import path
from . import views
from .views import ProductViewSet



urlpatterns = [
    path('', views.home_product, name='products_list'),
    path('<int:pk>/', views.product_detail, name='product_room'),
    path('rate_product/<int:pk>/', views.rate_product, name='rate_product'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='product-detail'),
]

