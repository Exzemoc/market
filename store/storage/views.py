from django.shortcuts import render, get_object_or_404
from .models import Product, Rating
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Avg
from orders.models import Cart, ProductInCart


def products_list(request):
    products = Product.objects.filter(is_active=True).order_by('-created')[:]
    context = {'products': products}
    return render(request, 'storage/products_list.html', context)


# Вывод информации о товаре в комантау товара
@login_required(login_url='/users/login/')
def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    already_rated = Rating.objects.filter(product=product, user=request.user).exists()
    average_rating = Rating.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']

    context = {
        'product': product,
        'already_rated': already_rated,
        'average_rating': average_rating,
    }
    return render(request, 'storage/product_room.html', context)


# Добавление рейтинга товара
@login_required(login_url='/users/login/')
def rate_product(request, pk):
    if request.method == 'POST':
        rating_value = int(request.POST['rating'])
        product = get_object_or_404(Product, pk=pk)
        rating, created = Rating.objects.get_or_create(product=product, user=request.user)
        rating.rating = rating_value
        rating.save()
    return redirect('product_room', pk=pk)


# Добавление нужного кол-во товара в корзину
@login_required(login_url='/users/login/')
def add_to_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    quantity = int(request.POST.get('quantity', 1))

    # Получение или создание корзины пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Получение или создание записи о товаре в корзине
    try:
        product_in_cart = ProductInCart.objects.get(cart=cart, product=product)
        product_in_cart.quantity += quantity
        product_in_cart.save(update_fields=['quantity'])
    except ProductInCart.DoesNotExist:
        product_in_cart = ProductInCart.objects.create(cart=cart, product=product, name=product.name,
                                                       price=product.price, quantity=quantity)

    cart.total_items += quantity
    cart.total_price += (product.price * quantity)
    cart.save()

    return redirect('product_room', pk=pk)


def home_product(request):
    title = 'Список товаров'
    latest_products = Product.objects.filter(is_active=True)

    # Получение параметров фильтрации из запроса
    date_release = request.GET.get('date_release')
    tip = request.GET.get('tip')
    name = request.GET.get('name')
    price_from = request.GET.get('price_from')
    price_to = request.GET.get('price_to')
    # Применение фильтров, если они указаны

    if date_release:
        latest_products = latest_products.filter(date_release=date_release)
    if tip:
        latest_products = latest_products.filter(tip=tip)
    if name:
        latest_products = latest_products.filter(name__icontains=name)
    if price_from:
        latest_products = latest_products.filter(price__gte=price_from)
    if price_to:
        latest_products = latest_products.filter(price__lte=price_to)
    context = {
        'title': title,
        'latest_products': latest_products,
    }
    return render(request, 'storage/products_list.html', context)
