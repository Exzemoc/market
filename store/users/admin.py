from django.contrib import admin
from .models import Wallet, Order
from orders.models import ProductInCart

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'address', 'comment', 'all_name', 'status']
