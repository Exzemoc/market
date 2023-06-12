from django.shortcuts import render
from storage.models import Product, ProductImage

def home(request):
    return render(request,'home/home_page.html')



# Вывод последних 10 добавленных товаров из модели Product
def home_product(request):
    latest_products = Product.objects.filter(is_active=True).order_by('-created')[:10]
    context = {'latest_products': latest_products}
    return render(request, 'home/home_page.html', context)

