from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, Payment
from users.models import Order
from orders.models import ProductInCart
from .serializers import PaymentSerializer, CartSerializer, ProductInCartSerializer
from rest_framework import viewsets


# Отображение корзины
def cart_view(request):
    user = request.user
    cart = Cart.objects.filter(user=user).first()
    context = {'cart': cart}
    return render(request, 'orders/cart.html', context)


# Представление оплаты
def payment_view(request):
    user = request.user
    cart = Cart.objects.get(user=user)

    if request.method == 'POST':

        cart = Cart.objects.get(user=user)
        amount = cart.total_price

        payment = Payment.objects.create(user=user, amount=amount)

        cart.payment = payment
        cart.delete()

        user.wallet.balance -= amount
        user.wallet.save()

        order = Order.objects.filter(user=user).latest('id')

        order.status = 'paid'
        order.save()

        return redirect('home')

    return render(request, 'orders/payment.html', {'cart': cart})

def delivery_choice(request):
    return render(request,'orders/delivery_choice.html')


def delivery_form(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        comment = request.POST.get('comment')
        product_in_cart_list = ProductInCart.objects.filter(cart=request.user.cart)

        order = Order.objects.create(
            user=request.user,
            phone=phone,
            address=address,
            comment=comment,
            status='unpaid'
        )

        all_names = []
        for product_in_cart in product_in_cart_list:
            name = product_in_cart.name
            quantity = product_in_cart.quantity
            name_with_quantity = f'{name}: {quantity} шт.'
            all_names.append(name_with_quantity)

        all_names_str = ', '.join(all_names)
        order.all_name = all_names_str
        order.save()

        return redirect('payment')  # Перенаправление на страницу оплаты

    return render(request, 'orders/delivery_form.html')


def clear_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user).first()
    if cart:
        cart.productincart_set.all().delete()
        # Обновить значения total_items и total_price в модели Cart
        cart.total_items = 0
        cart.total_price = 0
        cart.save()
    return redirect('cart')


def remove_from_cart(request, item_id):
    item = get_object_or_404(ProductInCart, id=item_id)
    cart = item.cart
    item.delete()
    # Обновить значения total_items и total_price в модели Cart
    cart.update_totals()
    cart.save()
    return redirect('cart')


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class ProductInCartViewSet(viewsets.ModelViewSet):
    queryset = ProductInCart.objects.all()
    serializer_class = ProductInCartSerializer
