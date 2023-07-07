from rest_framework import serializers
from orders.models import ProductInCart, Cart
from users.models import Order
from rest_framework.serializers import HyperlinkedModelSerializer


class ProductFilterSerializer(serializers.Serializer):
    date_release = serializers.IntegerField(required=False)
    tip = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    price_from = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
    price_to = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)


class ProductInCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCart
        fields = ['id', 'product', 'name', 'price', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['phone', 'address', 'comment']