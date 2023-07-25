from django.contrib import admin
from .models import Wallet, Order, PurchaseHistory
from orders.models import ProductInCart

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'address', 'comment', 'all_name', 'status']


@admin.register(PurchaseHistory)
class PurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'spent_amount', 'purchase_date', 'all_name' )