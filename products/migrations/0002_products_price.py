# Generated by Django 2.2.3 on 2019-08-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.CharField(default=50, max_length=100),
            preserve_default=False,
        ),
    ]
