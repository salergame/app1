# Generated by Django 4.2.7 on 2024-03-14 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_alter_filter_test_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_test',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.products', verbose_name='Продукт'),
        ),
    ]
