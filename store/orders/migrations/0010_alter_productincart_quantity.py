# Generated by Django 4.2.1 on 2023-06-11 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_productincart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productincart',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
