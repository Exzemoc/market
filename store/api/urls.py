from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home_api'),
    path('products_list/', views.ProductListView.as_view(), name='product_list_api'),
    path('user_balance/', views.UserBalanceAPIView.as_view(), name='user_balance_api'),
    path('cart/', views.CartView.as_view(), name='cart_api'),
    path('products_room/<int:product_id>/', views.ProductView.as_view(), name='products_room_api'),
    path('delivery_form/', views.OrderCreateView.as_view(), name='delivery_form_api'),
    path('payment/', views.PaymentConfirmationView.as_view(), name='payment_api'),
]