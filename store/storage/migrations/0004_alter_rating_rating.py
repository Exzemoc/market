# Generated by Django 4.2.1 on 2023-06-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True),
        ),
    ]
