from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Wallet of {self.user.username}"


class Order(models.Model):
    STATUS_CHOICES = (
        ('paid', 'Оплачено'),
        ('unpaid', 'Не оплачено'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unpaid')
    is_confirmed = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    all_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"Заказ пользователя {self.user.username}, Статус: {self.get_status_display()}"




