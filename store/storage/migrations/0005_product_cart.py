# Generated by Django 4.2.1 on 2023-06-11 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_cart_remove_productinorder_order_and_more'),
        ('storage', '0004_alter_rating_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='orders.cart'),
        ),
    ]
