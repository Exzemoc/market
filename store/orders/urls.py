from django.urls import path
from . import views
from .views import PaymentViewSet, CartViewSet, ProductInCartViewSet


urlpatterns = [
    path('payment/', views.payment_view, name='payment'),
    path('', views.cart_view, name='cart'),
    path('delivery_choice/', views.delivery_choice, name='delivery_choice'),
    path('delivery_form/', views.delivery_form, name='delivery_form'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear/', views.clear_cart, name='clear_cart'),
    path('api/payment/', PaymentViewSet.as_view({'get': 'list', 'post': 'create'}), name='payment_api'),
    path('api/', CartViewSet.as_view({'get': 'list', 'post': 'create'}), name='cart_api'),
    path('api/product_in_cart/', ProductInCartViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='product_in_cart_api'),
]
