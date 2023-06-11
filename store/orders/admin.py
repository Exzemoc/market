from django.contrib import admin
from .models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_items', 'total_price']

admin.site.register(Cart, CartAdmin)