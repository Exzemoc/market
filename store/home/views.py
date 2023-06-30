from django.shortcuts import render, redirect
from users.models import Wallet
from storage.models import Product, ProductImage
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


def home(request):
    return render(request,'home/home_page.html')


def home_product(request):
    latest_products = Product.objects.filter(is_active=True).order_by('-created')[:10]
    context = {'latest_products': latest_products}
    return render(request, 'home/home_page.html', context)


# Вывод баланса для всех страниц

def layout_view(request):
    user = request.user
    wallet = Wallet.objects.get(user=user)
    balance = wallet.balance

    context = {
        'balance': balance,
    }
    return render(request, 'home/layout.html', context)





