from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from storage.serializers import ProductSerializer
from orders.models import Cart, ProductInCart, Payment
from storage.models import Product
from .serializers import  ProductFilterSerializer, ProductInCartSerializer, OrderSerializer
from users.models import Wallet, Order
from users.serializers import WalletSerializer
from decimal import Decimal



class HomeView(APIView):
    def get(self, request):
        latest_products = Product.objects.order_by('-id')[:10]
        serializer = ProductSerializer(latest_products, many=True)
        return Response(serializer.data)


# http://127.0.0.1:8000/api/products_list/?genre=Фантастика тест фильтра
class ProductListView(generics.ListAPIView):
    serializer_class = ProductFilterSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get('name')
        genre = self.request.query_params.get('genre')
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        price_from = self.request.query_params.get('price_from')
        price_to = self.request.query_params.get('price_to')

        if name:
            queryset = queryset.filter(name__icontains=name)
        if genre:
            queryset = queryset.filter(tip__icontains=genre)
        if date_from:
            queryset = queryset.filter(date_release__gte=date_from)
        if date_to:
            queryset = queryset.filter(date_release__lte=date_to)
        if price_from:
            queryset = queryset.filter(price__gte=price_from)
        if price_to:
            queryset = queryset.filter(price__lte=price_to)

        return queryset


class UserBalanceAPIView(RetrieveAPIView):
    serializer_class = WalletSerializer

    def get_object(self):
        user = self.request.user
        wallet, _ = Wallet.objects.get_or_create(user=user)
        return wallet


class CartView(APIView):
    def get(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user).first()
        serializer = ProductInCartSerializer(cart.productincart_set.all(), many=True)
        total_price = cart.total_price
        total_items = cart.total_items
        response_data = {
            'cart': serializer.data,
            'total_price': total_price,
            'total_items': total_items
        }
        return Response(response_data)

    def delete(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user).first()
        cart.productincart_set.all().delete()
        cart.total_price = 0
        cart.total_items = 0
        cart.save()
        return Response({'message': 'Cart cleared successfully.'})


# POST = добавить в cart
class ProductView(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        user = request.user

        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            # Создать новую корзину для пользователя, если она не существует
            cart = Cart.objects.create(user=user)

        cart = Cart.objects.filter(user=request.user).first()
        item = ProductInCart.objects.filter(cart=cart, product=product).first()

        if item:
            item.quantity += 1
            item.save()
        else:
            item = ProductInCart.objects.create(cart=cart, product=product, name=product.name, price=product.price, quantity=1)

        return Response({'message': 'Товар успешно добавлен в корзину.'})


# {"phone": "123456789", "address": "Москва", "comment": "Оплата наличными"} для теста
class OrderCreateView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message': 'Заказ успешно оформлен.'}, status=201)
        else:
            return Response(serializer.errors, status=400)


class PaymentConfirmationView(APIView):
    def post(self, request):
        # Получить данные о платеже из запроса
        amount = request.data.get('amount')
        user = request.user

        payment = Payment(amount=amount, user=user)
        payment.is_successful = True
        payment.save()

        # Создать платеж и сохранить его в базе данных
        wallet = Wallet.objects.get(user=user)
        amount = Decimal(amount)
        wallet.balance -= amount
        wallet.save()

        if payment.is_successful:
            wallet = Wallet.objects.get(user=user)
            wallet.balance -= Decimal(amount)
            wallet.save()

            # Получить корзину пользователя
            cart = Cart.objects.get(user=user)

            # Удалить все объекты ProductInCart, связанные с корзиной
            ProductInCart.objects.filter(cart=cart).delete()

            # Обновить статус заказа на "Оплачено", если он существует
            orders = Order.objects.filter(user=user)
            if orders.exists():
                order = orders.first()
                order.status = 'paid'
                order.save()

        # Обновить статус заказа на "Оплачено"
        order = Order.objects.get(user=user, status='unpaid')
        order.status = 'paid'
        order.save()

        # Подготовить данные для ответа
        wallet_serializer = WalletSerializer(wallet)
        order_serializer = OrderSerializer(order)
        response_data = {
            'message': 'Оплата успешно подтверждена.',
            'wallet': wallet_serializer.data,
            'order': order_serializer.data
        }

        # Возвращаем успешный ответ с данными о платеже
        return Response(response_data, status=status.HTTP_200_OK)