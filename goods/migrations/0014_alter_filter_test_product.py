# Generated by Django 4.2.7 on 2024-03-15 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0013_alter_filter_test_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_test',
            name='product',
            field=models.ForeignKey(limit_choices_to={'category_id': 5}, on_delete=django.db.models.deletion.CASCADE, to='goods.products', verbose_name='Продукт'),
        ),
    ]
