from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, Payment


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

        return redirect('home')

    return render(request, 'orders/payment.html', {'cart': cart})
