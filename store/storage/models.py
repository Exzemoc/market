from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from orders.models import Cart

class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_release = models.IntegerField(default=0)
    tip = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.CharField(max_length=228, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    def average_rating(self):
        return self.rating_set.aggregate(Avg('rating'))['rating__avg']

    def __str__(self):
        return "%s, %s" % (self.price, self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='media/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __STR__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')), null=True, default=0)

    class Meta:
        unique_together = (('product', 'user'),)
