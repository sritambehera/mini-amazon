# Generated by Django 2.2.3 on 2019-09-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0011_remove_usercart_cart_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercart',
            name='cart_item',
            field=models.CharField(max_length=50, null=True),
        ),
    ]