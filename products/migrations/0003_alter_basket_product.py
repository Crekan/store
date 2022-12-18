# Generated by Django 4.1.4 on 2022-12-18 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name=''),
        ),
    ]