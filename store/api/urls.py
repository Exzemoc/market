from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'products', ProductViewsSet, basename='product')
router.register(r'ratings', RatingViewsSet, basename='rating')
router.register(r'product_images', ProductImageViewsSet, basename='product_image')
router.register(r'wallets', WalletViewsSet, basename='wallet')
router.register(r'orders', OrderViewsSet, basename='order')
router.register(r'users', UserViewsSet, basename='user')
router.register(r'payments', PaymentViewsSet, basename='payment')
router.register(r'carts', CartViewsSet, basename='cart')
router.register(r'products_in_cart', ProductInCartViewsSet, basename='product_in_cart')

urlpatterns = [
    path('home/', HomeView.as_view(), name='home_api'),
    path('', include(router.urls)),
]