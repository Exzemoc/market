from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
from .serializers import *
from orders.models import ProductInCart, Cart, Payment
from users.models import Order, Wallet
from storage.models import Product, ProductImage, Rating


@permission_classes([IsAdminUser])
class HomeView(APIView):
    def get(self, request):
        user = request.user
        if user.is_superuser:
            latest_products = Product.objects.order_by('-id')[:10]
            serializer = ProductSerializer(latest_products, many=True)
            return Response(serializer.data)
        else:
            return HttpResponse('У вас нет доступа к этой странице.')


class ProductViewsSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class RatingViewsSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAdminUser]


class ProductImageViewsSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminUser]


class WalletViewsSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsAdminUser]


class OrderViewsSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]


class UserViewsSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class PaymentViewsSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAdminUser]


class CartViewsSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAdminUser]


class ProductInCartViewsSet(viewsets.ModelViewSet):
    queryset = ProductInCart.objects.all()
    serializer_class = ProductInCartSerializer
    permission_classes = [IsAdminUser]
