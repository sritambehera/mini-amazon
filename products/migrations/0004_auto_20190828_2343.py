# Generated by Django 2.2.3 on 2019-08-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_products_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='items',
            field=models.FileField(upload_to='assets/'),
        ),
    ]
