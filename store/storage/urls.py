from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('<int:pk>', views.PruductView.as_view(), name='product_room'),
]