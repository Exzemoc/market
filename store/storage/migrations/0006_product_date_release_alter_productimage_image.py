# Generated by Django 4.2.1 on 2023-07-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0005_product_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_release',
            field=models.IntegerField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
