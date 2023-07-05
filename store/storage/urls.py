from django.urls import path
from . import views
from .views import ProductViewSet, RatingViewSet, ProductImageViewSet


urlpatterns = [
    path('', views.home_product, name='products_list'),
    path('<int:pk>/', views.product_detail, name='product_room'),
    path('rate_product/<int:pk>/', views.rate_product, name='rate_product'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('api/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list_api'),
    path('api/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update',
                                                  'delete': 'destroy'}), name='product-detail_api'),
    path('api/product_image/', ProductImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_image_api'),
    path('api/rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_rating_api'),
]

