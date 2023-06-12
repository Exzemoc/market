from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cart


# Отображение корзины
def cart_view(request):
    user = request.user
    cart = Cart.objects.filter(user=user).first()
    context = {'cart': cart}
    return render(request, 'orders/cart.html', context)
