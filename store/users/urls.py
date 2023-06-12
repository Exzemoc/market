from django.urls import path
from . import views

urlpatterns = [
    path('balance/', views.user_balance, name='balance'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]