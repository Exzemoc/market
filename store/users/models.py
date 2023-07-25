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

    DELIVERY_STATUS_CHOICES = (
        ('pending', 'Ожидает доставки'),
        ('in_transit', 'В пути'),
        ('delivered', 'Доставлен'),
    )

    delivery_status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES, default='pending')


    def save(self, *args, **kwargs):
        if self.status == 'paid' and not self.pk:
            # Создаем запись в модели PurchaseHistory при изменении статуса на "оплачено" и сохранении нового заказа
            PurchaseHistory.objects.create(user=self.user, spent_amount=self.total_amount, purchase_date=self.date)
        super().save(*args, **kwargs)

    def get_status_display_ru(self):
        return 'Оплачено' if self.status == 'paid' else 'Не оплачено'

    def get_delivery_status_display_ru(self):
        if self.delivery_status == 'pending':
            return 'Ожидает доставки'
        elif self.delivery_status == 'in_transit':
            return 'В пути'
        elif self.delivery_status == 'delivered':
            return 'Доставлен'
        else:
            return 'Неизвестный статус доставки'


    def __str__(self):
        return f"Заказ пользователя {self.user.username}, Статус: {self.get_status_display()}"


class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)
    all_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"Покупка пользователя {self.user.username}, сумма: {self.spent_amount}, дата: {self.purchase_date}"


def create_purchase_history(user, amount):
    # Найти последний заказ пользователя
    latest_order = Order.objects.filter(user=user).latest('id')

    # Создать новую запись PurchaseHistory с данными из последнего заказа
    PurchaseHistory.objects.create(
        user=user,
        spent_amount=amount,
        all_name=latest_order.all_name
    )
