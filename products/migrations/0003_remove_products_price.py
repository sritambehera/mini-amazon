# Generated by Django 2.2.3 on 2019-08-26 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
    ]
