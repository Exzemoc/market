from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Платеж пользователя {self.user.username} на сумму {self.amount}"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_items = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

class ProductInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('storage.Product', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.name} - Количество: {self.quantity} - Цена: {self.price}"


