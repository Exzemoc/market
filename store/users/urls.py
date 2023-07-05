from django.urls import path
from . import views
from .views import WalletViewSet, OrderViewSet, UserViewSet

urlpatterns = [
    path('balance/', views.user_balance, name='balance'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/wallet/', WalletViewSet.as_view({'get': 'list', 'post': 'create'}), name='wallet_api'),
    path('api/order/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='order_api'),
    path('api/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='users_api')
]