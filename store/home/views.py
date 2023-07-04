from django.db.models import Avg
from django.shortcuts import render, redirect
from users.models import Wallet
from storage.models import Product, ProductImage, Rating


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


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    average_rating = Rating.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']
    context = {
        'product': product,
        'average_rating': average_rating,
    }
    return render(request, 'home/home_page.html', context)



