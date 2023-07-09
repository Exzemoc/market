from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from orders.models import ProductInCart, Cart, Payment
from users.models import Order, Wallet
from storage.models import Product, ProductImage, Rating


class HomeView(APIView):
    def get(self, request):
        latest_products = Product.objects.order_by('-id')[:10]
        serializer = ProductSerializer(latest_products, many=True)
        return Response(serializer.data)


class ProductViewsSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RatingViewsSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class ProductImageViewsSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class WalletViewsSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class OrderViewsSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserViewsSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentViewsSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class CartViewsSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class ProductInCartViewsSet(viewsets.ModelViewSet):
    queryset = ProductInCart.objects.all()
    serializer_class = ProductInCartSerializer
