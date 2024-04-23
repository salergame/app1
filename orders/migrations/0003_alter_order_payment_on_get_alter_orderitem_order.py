# Generated by Django 5.0.2 on 2024-04-22 08:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_delivery_addres_order_delivery_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_on_get',
            field=models.BooleanField(default=False, verbose_name='Оплата при получении'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ'),
        ),
    ]
