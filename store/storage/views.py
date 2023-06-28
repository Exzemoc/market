from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Product, Rating
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Avg
from orders.models import Cart, ProductInCart
from django.db.models import F


def products_list(request):
    products = Product.objects.filter(is_active=True).order_by('-created')[:]
    context = {'products': products}
    return render(request, 'storage/products_list.html', context)


class PruductView(DetailView):
    model = Product
    template_name = 'storage/product_room.html'
    context_object_name = 'product'


# Вывод информации о товаре в комантау товара
@login_required
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
def rate_product(request, pk):
    if request.method == 'POST':
        rating_value = int(request.POST['rating'])
        product = get_object_or_404(Product, pk=pk)
        rating, created = Rating.objects.get_or_create(product=product, user=request.user)
        rating.rating = rating_value
        rating.save()
    return redirect('product_room', pk=pk)


# Добавление нужного кол-во товара в корзину
def add_to_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    quantity = int(request.POST.get('quantity', 1))

    if quantity < 1:
        messages.error(request, 'Недопустимое количество товара.')
        return redirect('product_room', pk=pk)

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
