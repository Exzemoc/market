# Generated by Django 4.2.1 on 2023-06-05 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_productinorder_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinorder',
            name='nmb',
            field=models.IntegerField(default=1),
        ),
    ]