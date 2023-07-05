from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Wallet, Order
from .serializers import WalletSerializer, OrderSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Wallet.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/registr.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


# Выводит бланс пользователя
def user_balance(request):
    user = request.user

    try:
        wallet = Wallet.objects.get(user=user)
        balance = wallet.balance
    except Wallet.DoesNotExist:
        # Обработка случая, когда кошелек не существует
        balance = 0

    context = {
        'balance': balance
    }
    return render(request, 'users/balance.html', {'balance': balance})


#API баланса
class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


#API доставки
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


#API юзеров
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



